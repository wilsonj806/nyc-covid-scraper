import json
from selenium import webdriver
from bs4 import BeautifulSoup
# import pandas as pd

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

jsonData = json.load(open('data.json', 'r'))
print(jsonData)

driver.get('https://www1.nyc.gov/site/doh/health/health-topics/coronavirus.page')

content = driver.page_source

soup = BeautifulSoup(content, features = "html.parser")
for td in soup.findAll('td', href = False, attrs = { 'data-label': 'People Tested Positive in NYC'}):
  strong = td.find('strong').text.split()[0]

  print(strong)


driver.close()