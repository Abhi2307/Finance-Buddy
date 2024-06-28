import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the historical stock data
stock_data = pd.read_csv('stock_data.csv')

# Prepare data
X = stock_data[['Open', 'High', 'Low', 'Volume']].values
y = stock_data['Close'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict returns
y_pred = model.predict(X_test)
print(y_pred)

