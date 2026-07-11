import json
import os
import exp_fun

ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n"))   
             
while not ures == 6:
    if ures == 1:
        exp_fun.add_expense(ures)
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n")) 
    elif ures == 2:
        exp_fun.   show_expenses(ures)
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n")) 
    elif ures == 3:
        exp_fun.calculate_total(ures)
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n"))
    elif ures == 4:
        exp_fun.serch_expense(ures)
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n"))
    elif ures == 5:
        exp_fun.delete_expense(ures)
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n"))
    else:
        print("Invalid option. Please try again.")
        ures = int(input("1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Exit\n"))
print("Thank you for using Espense Tracker")
