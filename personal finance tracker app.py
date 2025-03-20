import tkinter as tk
from tkinter import ttk, messagebox

class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("600x500")

        # Initialize budget values
        self.total_income = 0
        self.total_expenses = 0
        self.categories = {}

        # Title Label
        tk.Label(root, text="Finance Tracker", font=("Arial", 14, "bold")).pack()

        # Current Budget Display
        self.budget_label = tk.Label(root, text=f"Current Budget: {self.total_income - self.total_expenses}",
                                     font=("Arial", 12), bg="lightblue", width=30, height=2)
        self.budget_label.pack(pady=10)

        # Buttons to Add Income, Expenses, and Categories
        btn_frame = tk.Frame(root)
        btn_frame.pack()
        tk.Button(btn_frame, text="Add Expense", command=self.add_expense).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Add Income", command=self.add_income).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Add Category", command=self.add_category).grid(row=0, column=2, padx=5)

        # Category List
        self.category_frame = tk.Frame(root)
        self.category_frame.pack(pady=10)
        self.update_category_list()

        # Total Income & Expenses Display
        self.income_label = tk.Label(root, text=f"Total Income: {self.total_income}", fg="green")
        self.income_label.pack()
        self.expense_label = tk.Label(root, text=f"Total Expenses: {self.total_expenses}", fg="red")
        self.expense_label.pack()

        # Transaction Table
        self.transactions_list = ttk.Treeview(root, columns=("Category", "Amount"), show="headings")
        self.transactions_list.heading("Category", text="Category")
        self.transactions_list.heading("Amount", text="Amount")
        self.transactions_list.pack(pady=10)

    def add_income(self):
        amount = self.get_amount("Enter Income Amount:")
        if amount is not None:
            self.total_income += amount
            self.transactions_list.insert("", "end", values=("Income", amount))
            self.update_display()

    def add_expense(self):
        if not self.categories:
            messagebox.showwarning("Warning", "Please add a category first!")
            return
        
        category, amount = self.get_category_and_amount()
        if category and amount is not None:
            self.categories[category] += amount
            self.total_expenses += amount
            self.transactions_list.insert("", "end", values=(category, -amount))
            self.update_display()

    def add_category(self):
        category = self.get_input("Enter Category Name:")
        if category and category not in self.categories:
            self.categories[category] = 0
            self.update_category_list()

    def get_input(self, prompt):
        input_win = tk.Toplevel(self.root)
        input_win.title("Input")
        tk.Label(input_win, text=prompt).pack()
        entry = tk.Entry(input_win)
        entry.pack()
        
        def submit():
            input_win.result = entry.get()
            input_win.destroy()
        
        tk.Button(input_win, text="Submit", command=submit).pack()
        input_win.result = None
        input_win.wait_window()
        return input_win.result

    def get_amount(self, prompt):
        amount = self.get_input(prompt)
        try:
            return float(amount) if amount else None
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return None

    def get_category_and_amount(self):
        category_win = tk.Toplevel(self.root)
        category_win.title("Select Category & Amount")
        tk.Label(category_win, text="Select Category:").pack()

        category_var = tk.StringVar(category_win)
        category_var.set(list(self.categories.keys())[0])
        category_menu = tk.OptionMenu(category_win, category_var, *self.categories.keys())
        category_menu.pack()
        
        tk.Label(category_win, text="Enter Amount:").pack()
        amount_entry = tk.Entry(category_win)
        amount_entry.pack()
        
        def submit():
            category_win.result = (category_var.get(), amount_entry.get())
            category_win.destroy()
        
        tk.Button(category_win, text="Submit", command=submit).pack()
        category_win.result = (None, None)
        category_win.wait_window()
        try:
            return category_win.result[0], float(category_win.result[1])
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return None, None

    def update_category_list(self):
        for widget in self.category_frame.winfo_children():
            widget.destroy()
        for category in self.categories:
            tk.Label(self.category_frame, text=f"{category}: {self.categories[category]}", bg="grey").pack()
    
    def update_display(self):
        self.budget_label.config(text=f"Current Budget: {self.total_income - self.total_expenses}")
        self.income_label.config(text=f"Total Income: {self.total_income}")
        self.expense_label.config(text=f"Total Expenses: {self.total_expenses}")
        self.update_category_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()
