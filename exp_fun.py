import json
import os


if os.path.exists("expense.json"):
    with open("expense.json","r") as file:
        expense = json.load(file)
else:
        expense = {"FOOD": "300", "ELECTRICITY": "400"}


def add_expense(ures):
    if ures == 1:
        addkey = input("What write your type of expense: ")
        try:
            addval = float(input("please type the amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print("Returning to main menu...")
            return
        try:
            exit = input(f"add {addkey} for amount of ${addval} ? (y/n): ")
            if exit.lower() == "y":
                expense[addkey] = addval
                print(f"Expense added: {addkey} for ${addval}")
            else:
                print("Expense not added.")
        except TypeError as e:
            print(f"An error occurred: {e}")
        finally:
            with open("expense.json","w") as file:
                json.dump(expense, file, indent=4)
            print("Save and Returning to main menu...")
def show_expenses(ures):
     if ures == 2:
        for name,value in expense.items():
            print(f"{name} : ${value}")
def calculate_total(ures):        
    if ures == 3:
        total = 0
        for name,value in expense.items():
            total += float(value)
        print(f"total : ${total}")
def serch_expense(ures):
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