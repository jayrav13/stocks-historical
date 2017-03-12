# Import statements
import csv
import sys
import urllib2
import requests
import json
from datetime import date, timedelta


year = None
if len(sys.argv) > 1:
	year = sys.argv[1]
else:
	year = 1980

filename = None
if len(sys.argv) > 2:
	filename = sys.argv[2]
else:
	filename = 'result.json'

# Return data from CSV.
def get_csv(url, delimiter=","):
	response = requests.get(url)
	data = csv.DictReader(response.text.split('\n'), delimiter=delimiter)
	return data

# Generate URL for ticker-specific historical data.
def generate_url(ticker):
	return "http://chart.finance.yahoo.com/table.csv?s=%s&a=0&b=1&c=%s&g=d&ignore=.csv" % (ticker, year)

# Pull all tickers in CSV
tickers = get_csv('http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download')

# Set up data array.
data = []

# Add to data array, making this a 2D array.
for ticker in tickers:
	historical = get_csv( generate_url( ticker["Symbol"] ) )

	ticker['history'] = []

	for history in historical:
		ticker['history'].append(history)

	data.append(ticker)
	print ticker["Symbol"] + " - " + ticker["Name"]

f = open(filename, 'w')
f.write(json.dumps(data, indent=4, sort_keys=True))
f.close()



