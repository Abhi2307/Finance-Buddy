import yfinance as yf
import requests
import json

# Fetch historical stock data from Yahoo Finance
stock_data = yf.download('AAPL', start='2020-01-01', end='2023-01-01')
stock_data.to_csv('stock_data.csv')

# Fetch market sentiment data from a news API
response = requests.get('https://newsapi.org/v2/everything?q=stock+market&apiKey=YOUR_API_KEY')
news_data = response.json()
with open('news_data.json', 'w') as f:
    json.dump(news_data, f)
