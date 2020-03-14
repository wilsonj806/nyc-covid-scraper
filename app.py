import csv
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def init_ping():
  return "NYC Covid19 Scraper; Version 0.0.0"


@app.route('/data')
def fetch_data():
  with open('data.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter = ' ')
    data = ''
    for row in reader:
      dataRow = ', '.join(row)
      data += dataRow
      data += '\n'
    return data