import json
import os
from exp_class import eplass


expenses = []

if os.path.exists("expense.json"):
    with open("expense.json", "r") as file:
        try:
            raw_data = json.load(file)
            # If the JSON contains a list, convert each dict back into an OOP object
            if isinstance(raw_data, list):
                expenses = [
                    eplass(
                        amount=item["amount"],
                        category=item["category"],
                        date=item["date"],
                    )
                    for item in raw_data
                ]
            # If the JSON is still using your old dictionary format, convert it safely
            elif isinstance(raw_data, dict):
                for key, val in raw_data.items():
                    expenses.append(eplass(amount=val, category=key, date="2026-07-12"))
                    
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error reading JSON file ({e}). Starting with a clean list.")
            expenses = []
else:
    expenses = [
        eplass("FOOD", 300, "2026-07-12"),
        eplass("ELECTRICITY", 400, "2026-07-12",),
    ]

def save_to_json():
    with open("expense.json", "w") as file:
        json_ready_list = [exp.to_dict() for exp in expenses]
        json.dump(json_ready_list, file, indent=4)
        

def add_expense(ures):
    if ures == 1:
        category = input("Enter the category: ").upper()
        try:
            amount = float(input("Please type the amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
            return
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")    
        eplass_instance = eplass(amount, category, date)
        print("\nConfirm details:")
        eplass_instance.display()
        
        confirm = input("Add this expense? (y/n): ")
        if confirm.lower() == "y":
            expenses.append(eplass_instance)
            print("Expense added.")
            save_to_json()
        else:
            print("Expense not added.")
            
            
def show_expenses(ures):
    if ures == 2:
        if not expenses:
            if not expenses:
                print("No expenses recorded yet.")
                return
        print("\n=== CURRENT EXPENSES ===")
        for exp in expenses:
            exp.display()
            
def calculate_total(ures):
    if ures == 3:
        total = sum(exp.amount for exp in expenses)
        print(f"total : {total:.2f}")
    
    
def search_expense(ures):
    if ures == 4:
        expense_name = input("Enter the name of the expense to search: ").lower()
        found = False
        for exp in expenses:
            if exp.category.lower() == expense_name:
                exp.display()
                found = True
        if not found:
            print(f"Expense '{expense_name}' not found.")

def delete_expense(ures):
    if ures == 5:
        expense_name = input("Enter the name of the expense to delete: ").strip().lower() 
        found = False
        for exp in expenses:
            if exp.category.lower() == expense_name:
                expenses.remove(exp)
                print(f"Expense {expense_name.upper()} has been deleted.")
                save_to_json()
                found = True
                print("Save and Returning to main menu...")
                break
        if not found:
            print(f"Expense {expense_name} not found.")
        print("Returning to main menu...")
            

                 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        amount = input("Enter the amount: ")
        category = input("Enter the category: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        description = input("Enter a description: ")
        expense_name = input("Enter the name of the expense: ")
        expense[expense_name] = amount
        print(f"Expense '{expense_name}' added successfully.")
        with open("expense.json","w") as file:
            json.dump(expense, file, indent=4)
        print("Save and Returning to main menu...")
        
def show_expenses(ures):
    if ures == 2:
        if not expense:
            print("No expenses found.")
        else:
            for category, expenses in expense.items():
                print(f"\nCategory: {category}")
                for exp in expenses:
                    eplass(**exp).display()

def search_expense(ures):
    if ures == 4:
        expense_name = input("Enter the name of the expense to search: ")
        for name,value in expense.items():
            if name.lower() == expense_name.lower():
                print(f"Expense '{name}' found with amount: ${value}")
                break
        else:
                print(f"Expense '{expense_name}' not found.")
def delete_expense(ures):
    if ures == 5:
        expense_name = input("Enter the name of the expense to delete: ")
    for name in expense.keys():
           if name.lower() == expense_name.lower():
            del expense[name]
            print(f"Expense '{expense_name}' has been deleted.")
            with open("expense.json","w") as file:
                json.dump(expense, file, indent=4)
            print("Save and Returning to main menu...")
            break
    else:
        print(f"Expense '{expense_name}' not found.")
 '''   
