# ------------------------------------------------------
# Import packages needed for this exercise
# ------------------------------------------------------

from yahoofinancials import YahooFinancials
#import yfinance as yahoo #decided not to use this module/library
from urllib import request #handle HTTP requests
import io #handle strings
import datetime
import time
import pandas as pand

# ------------------------------------------------------
# Creating a list of stock ticker symbols of companies in the DJI
# Current companies listed in the DJI not adjusting for historical changes in listing
# Input into extracting the historical closing prices for these companies
# Ticker symbols taken from CNBC website on July 13, 2022
# ------------------------------------------------------

tick_sym = ["AXP", "AMGN", "AAPL", "BA", "CAT", "CSCO", "CVX", "GS", "HD",
            "HON", "IBM", "INTC", "JNJ", "KO", "JPM", "MCD", "MMM", "MRK",
            "MSFT", "NKE", "PG", "TRV", "UNH", "CRM", "VZ", "V", "WBA",
            "WMT", "DIS", "DOW"]

# ------------------------------------------------------
# Create start and end date for the historical data range
# ------------------------------------------------------

start_date = datetime.datetime(2012,1,1)
end_date = datetime.datetime(2021,12,31)

# ------------------------------------------------------
# Extract the historical closing prices for the stock symbols
# listed in tick_sym for the date range shown in start_date and end_date
# using a loop connecting to the Yahoo Finance API
# ------------------------------------------------------

# Create final dataframe before profiling containing ticker symbol, date, and closing price
closing_price = pand.DataFrame()

# Use loop to iterate through the 30 ticker symbols
for i in tick_sym:

    # Print the ticker symbol for the data being downloaded so can montior progress
    print(" " + str(tick_sym.index(i)) + " " + i, sep=',', end=',', flush=True)
    



# code below works but need to integrate with other objects created and for loop
#yahoo_financials = YahooFinancials('AAPL')
#data = yahoo_financials.get_historical_price_data(start_date='2022-01-01', 
#                                                  end_date='2022-01-31', 
#                                                  time_interval='daily')
#print(pand.DataFrame(data['AAPL']['prices']))

# ------------------------------------------------------
# Profile the data
# ------------------------------------------------------

# ------------------------------------------------------
# Use LSTM
# ------------------------------------------------------

# ------------------------------------------------------
# Old snippets of code
# ------------------------------------------------------

#    stock = []
# stock = yahoo.download(start=start_date, end=end_date, progress=False)
#aapl= yf.Ticker("aapl")
#aapl_historical = aapl.history(start="2022-05-18", end="2022-07-15", interval="1d", actions = "false")