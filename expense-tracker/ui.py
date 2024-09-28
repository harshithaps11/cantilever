import tkinter as tk
from tkinter import messagebox, ttk
from db import add_expense, get_expenses
from utils import validate_date
from visualization import plot_expenses_by_category, predict_future_expenses

def create_main_window():
    root = tk.Tk()
    root.title("Expense Tracker")
    root.geometry("400x500")  # Adjust window size
    root.configure(bg="#f0f0f0")  # Background color

    # Style Configuration
    style = ttk.Style()
    style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
    style.configure("TButton", background="#007BFF", foreground="white", font=("Arial", 12))
    style.map("TButton", background=[('active', '#0056b3')])
    
    # Frame for the input area
    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(pady=20)

    def submit_expense():
        amount = amount_entry.get()
        category = category_entry.get()
        description = description_entry.get()
        date = date_entry.get()

        if not (amount and category and date):
            messagebox.showerror("Input Error", "All fields are required!")
            return

        if not validate_date(date):
            messagebox.showerror("Input Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        try:
            add_expense(float(amount), category, description, date)
            messagebox.showinfo("Success", "Expense added successfully!")
            clear_entries()
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number.")

    def clear_entries():
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)

    # Input fields with padding and style
    tk.Label(frame, text="Amount").pack(pady=5)
    amount_entry = tk.Entry(frame, font=("Arial", 12))
    amount_entry.pack(pady=5)

    tk.Label(frame, text="Category").pack(pady=5)
    category_entry = tk.Entry(frame, font=("Arial", 12))
    category_entry.pack(pady=5)

    tk.Label(frame, text="Description").pack(pady=5)
    description_entry = tk.Entry(frame, font=("Arial", 12))
    description_entry.pack(pady=5)

    tk.Label(frame, text="Date (YYYY-MM-DD)").pack(pady=5)
    date_entry = tk.Entry(frame, font=("Arial", 12))
    date_entry.pack(pady=5)

    # Add button
    add_button = ttk.Button(frame, text="Add Expense", command=submit_expense)
    add_button.pack(pady=20)

    # Display expenses button
    display_button = ttk.Button(frame, text="Display Expenses", command=lambda: print(get_expenses()))
    display_button.pack(pady=5)

    # Visualization buttons
    category_plot_button = ttk.Button(frame, text="Plot Expenses by Category", command=plot_expenses_by_category)
    category_plot_button.pack(pady=5)

    prediction_button = ttk.Button(frame, text="Predict Future Expenses", command=predict_future_expenses)
    prediction_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
