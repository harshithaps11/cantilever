import matplotlib.pyplot as plt
import pandas as pd
from db import get_expenses
from sklearn.linear_model import LinearRegression
import numpy as np

def plot_expenses_by_category():
    expenses = get_expenses()
    if not expenses:
        print("No expenses to visualize.")
        return

    df = pd.DataFrame(expenses, columns=['id', 'amount', 'category', 'description', 'date'])
    report_data = df.groupby('category')['amount'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.bar(report_data['category'], report_data['amount'], color='skyblue')
    plt.title('Total Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def predict_future_expenses():
    expenses = get_expenses()
    if not expenses:
        print("No expenses to analyze.")
        return

    df = pd.DataFrame(expenses, columns=['id', 'amount', 'category', 'description', 'date'])
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    monthly_expenses = df.resample('M').sum()

    # Prepare data for ML
    monthly_expenses['Month'] = np.arange(len(monthly_expenses))
    X = monthly_expenses[['Month']]
    y = monthly_expenses['amount']

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict future expenses
    future_months = np.array([[len(monthly_expenses) + i] for i in range(1, 7)])  # Predicting for next 6 months
    predictions = model.predict(future_months)

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_expenses.index, monthly_expenses['amount'], label='Historical Expenses', marker='o')
    future_dates = pd.date_range(start=monthly_expenses.index[-1] + pd.DateOffset(months=1), periods=6, freq='M')
    plt.plot(future_dates, predictions, label='Predicted Expenses', marker='o', color='orange')
    plt.title('Expense Prediction for Next 6 Months')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.legend()
    plt.tight_layout()
    plt.show()
