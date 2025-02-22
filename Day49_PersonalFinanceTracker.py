import tkinter as tk
from tkinter import messagebox

class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        
        # Initialize variables
        self.balance = 0
        
        # Create UI elements
        self.income_label = tk.Label(root, text="Income:")
        self.income_label.grid(row=0, column=0)
        
        self.income_entry = tk.Entry(root)
        self.income_entry.grid(row=0, column=1)
        
        self.expense_label = tk.Label(root, text="Expense:")
        self.expense_label.grid(row=1, column=0)
        
        self.expense_entry = tk.Entry(root)
        self.expense_entry.grid(row=1, column=1)
        
        self.add_income_button = tk.Button(root, text="Add Income", command=self.add_income)
        self.add_income_button.grid(row=0, column=2)
        
        self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=1, column=2)
        
        self.balance_label = tk.Label(root, text="Balance: $0")
        self.balance_label.grid(row=2, column=0, columnspan=3)
        
    def add_income(self):
        try:
            income = float(self.income_entry.get())
            self.balance += income
            self.update_balance()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
        
    def add_expense(self):
        try:
            expense = float(self.expense_entry.get())
            self.balance -= expense
            self.update_balance()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
    
    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")
        self.income_entry.delete(0, tk.END)
        self.expense_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()
