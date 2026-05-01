import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_data(file):
    df = pd.read_csv(file)
    amounts = df['amount'].values

    total = np.sum(amounts)
    avg = np.mean(amounts) if len(amounts) > 0 else 0

    return total, avg

def create_graph(file):
    df = pd.read_csv(file)
    category_sum = df.groupby('category')['amount'].sum()

    plt.figure()
    category_sum.plot(kind='pie', autopct='%1.1f%%')
    plt.ylabel('')
    plt.title('Expense Distribution')

    plt.savefig('static/graph.png')
    plt.close()