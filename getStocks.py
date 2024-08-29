import yfinance as yf
import pandas as pd

def download_stock_data(tickers, start_date, end_date):
    stock_data = {}
    for ticker in tickers:
        stock = yf.download(ticker, start=start_date, end=end_date)
        stock_data[ticker] = stock
    return stock_data

def save_to_excel(stock_data, file_name):
    with pd.ExcelWriter(file_name) as writer:
        for ticker, data in stock_data.items():
            data.to_excel(writer, sheet_name=ticker)

def main():
    # Define the list of tickers
    tickers = ['AAPL', 'MSFT', 'GOOGL']

    # Define the start and end dates for the data
    start_date = '2020-01-01'
    end_date = '2024-01-01'

    # Download stock data
    stock_data = download_stock_data(tickers, start_date, end_date)

    # Save data to Excel file
    save_to_excel(stock_data, 'stock_data.xlsx')

if __name__ == "__main__":
    main()
