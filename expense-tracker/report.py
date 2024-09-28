import matplotlib.pyplot as plt
import pandas as pd
from db import get_expenses

def generate_report():
    expenses = get_expenses()
    if not expenses:
        print("No expenses to report.")
        return

    df = pd.DataFrame(expenses, columns=['id', 'amount', 'category', 'description', 'date'])
    report_data = df.groupby('category')['amount'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.pie(report_data['amount'], labels=report_data['category'], autopct='%1.1f%%')
    plt.title('Spending by Category')
    plt.show()
