# ------------------------------------------------------
# Import packages needed for this exercise
# ------------------------------------------------------

import yfinance as yahoo
import requests #handle HTTP requests
import io #handle strings
import datetime
import time
import pandas as pand

# ------------------------------------------------------
# Creating a list of stock ticker symbols of companies in the DJI
# Current companies listed in the DJI not adjusting for historical changes in listing
# Input into extracting the historical closing prices for these companies
# ------------------------------------------------------

tick_sym = ["AXP", "AMGN", "AAPL", "BA", "CAT", "CSCO", "CVX", "GS", "HD",
            "HON", "IBM", "INTC", "JNJ", "KO", "JPM", "MCD", "MMM", "MRK",
            "MSFT", "NKE", "PG", "TRV", "UNH", "CRM", "VZ", "V", "WBA",
            "WMT", "DIS"]

# ------------------------------------------------------
# Create start and end date for the historical data range
# ------------------------------------------------------

start_date = datetime.datetime(2012,1,1)
end_date = datetime.datetime(2021,12,31)
