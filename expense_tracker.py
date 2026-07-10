import json
import os

if os.path.exists("expense.json"):
    with open("expense.json","r") as file:
        expense = json.load(file)
else:
        expense = {"FOOD": "300", "ELECTRICITY": "400"}

ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n"))

 

def add_expense(ures):
    if ures == 1:
        addkey = input("What write your type of expense: ")
        addval = input("please type the amount:")
        exit = input(f"add {addkey} for amount of ${addval} ? (y/n): ")
        if exit.lower() == "y":
            expense[addkey] = addval
            print(f"Expense added: {addkey} for ${addval}")
        else:
            print("Expense not added.")
def show_expenses(ures):
     if ures == 2:
        for name,value in expense.items():
            print(f"{name} : ${value}")
def calculate_total(ures):        
    if ures == 3:
        total = 0
        for name,value in expense.items():
            total += int(value)
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
            break
    else:
        print(f"Expense '{expense_name}' not found.")
        
             
while not ures == 6:
    if ures == 1:
        add_expense(ures)
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n")) 
    elif ures == 2:
        show_expenses(ures)
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n")) 
    elif ures == 3:
        calculate_total(ures)
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n"))
    elif ures == 4:
        serch_expense(ures)
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n"))
    elif ures == 5:
        delete_expense(ures)
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n"))
    else:
        print("Invalid option. Please try again.")
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n"))
print("Thank you for using Espense Tracker")
    



'''                   


    





      


#expense.update({"House":"1000"})
#expense.update({"FOOD":"500"})

for name,value in expense.items():
    print (f"{name} : ${value}")
    total += int(value)


print (f"total : ${total}")
 '''
 
 
with open("expense.json","w") as file:
    json.dump(expense, file, indent=4)
    print("Expense history has been updated!")
