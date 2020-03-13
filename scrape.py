import csv
from datetime import date
from selenium import webdriver
from bs4 import BeautifulSoup
# import pandas as pd

with webdriver.Chrome("/usr/local/bin/chromedriver") as driver:
  driver.get('https://www1.nyc.gov/site/doh/health/health-topics/coronavirus.page')

  content = driver.page_source

  todaysCount = None

  soup = BeautifulSoup(content, features = "html.parser")
  for div in soup.findAll('div', href = False, attrs = { 'style': 'padding:12px;background-color:#F0F0F0;line-height:1.4;'}):
    strong = div.find('strong').text.split('*')[0]
    todaysCount = strong

  driver.close()


with open('data.csv', 'a', newline='') as csvFile:
  fieldNames = ['date','count']
  today = date.today()
  writer = csv.DictWriter(csvFile, fieldnames = fieldNames)
  newRow = {
    'date': today,
    'count': todaysCount
  }
  writer.writerow(newRow)

