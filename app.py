from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from itsdangerous import URLSafeTimedSerializer as Serializer
import plotly.express as px
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
bcrypt = Bcrypt(app)

users = {}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users[username] = hashed_password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and bcrypt.check_password_hash(users[username], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'username' in session:
        # Load the historical stock data
        stock_data = pd.read_csv('stock_data.csv')

        # Ensure 'Date' column is in datetime format
        stock_data['Date'] = pd.to_datetime(stock_data['Date'])

        # Create portfolio performance visualization
        fig = px.line(stock_data, x='Date', y='Close', title='Portfolio Performance')
        graph = fig.to_html(full_html=False)
        return render_template('index.html', graph=graph, username=session['username'])
    else:
        return redirect(url_for('register'))

if __name__ == '__main__':
    app.run(debug=True)
