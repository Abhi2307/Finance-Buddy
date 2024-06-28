import pandas as pd
from pypfopt import EfficientFrontier, risk_models, expected_returns


# Load the historical stock data
stock_data = pd.read_csv('stock_data.csv')
# Convert 'date' column to datetime format (if not already)
stock_data['Date'] = pd.to_datetime(stock_data['Date'])

# Set 'date' column as the index
stock_data.set_index('Date', inplace=True)
# Calculate expected returns and risk
mu = expected_returns.mean_historical_return(stock_data)
S = risk_models.sample_cov(stock_data)

# Optimize portfolio
ef = EfficientFrontier(mu, S)
weights = ef.max_sharpe()
cleaned_weights = ef.clean_weights()
print(cleaned_weights)

