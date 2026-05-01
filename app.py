from flask import Flask, render_template, request, redirect
import pandas as pd
import os
from analyzer import analyze_data, create_graph
from models import Expense

app = Flask(__name__)
FILE = 'expenses.csv'

# Create CSV if not exists
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=['amount', 'category'])
    df.to_csv(FILE, index=False)

@app.route('/')
def index():
    df = pd.read_csv(FILE)
    return render_template('index.html', data=df.to_dict(orient='records'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']

        exp = Expense(amount, category)
        exp.save(FILE)

        return redirect('/')
    return render_template('add.html')

@app.route('/dashboard')
def dashboard():
    total, avg = analyze_data(FILE)
    create_graph(FILE)
    return render_template('dashboard.html', total=total, avg=avg)

if __name__ == '__main__':
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", "5000"))
    app.run(host=host, port=port, debug=True)
