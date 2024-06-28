import alpaca_trade_api as tradeapi

# Connect to Alpaca API
api = tradeapi.REST('PKDTRQ3GS2O8RZA9FHMU', 'NjPwRpcnzykwNxRqIps8jbS5ToFJVKFMDeTkHgjh', base_url='https://paper-api.alpaca.markets')

# Example weights from portfolio optimization
cleaned_weights = {'AAPL': 0.4, 'GOOGL': 0.3, 'AMZN': 0.3}

# Rebalance portfolio
for stock, weight in cleaned_weights.items():
    api.submit_order(
        symbol=stock,
        qty=int(weight * 100),
        side='buy',
        type='market',
        time_in_force='gtc'
    )


