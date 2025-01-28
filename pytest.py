import pandas as pd
import yfinance as yf

def fetch_stock_data(symbol, start_date, end_date):
    """
    Fetches historical stock data from Yahoo Finance.
    
    :param symbol: The stock symbol to fetch data for.
    :param start_date: The start date of the data in 'YYYY-MM-DD' format.
    :param end_date: The end date of the data in 'YYYY-MM-DD' format.
    :return: A pandas DataFrame containing the stock data.
    """
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data
