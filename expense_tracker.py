import json
import os


if os.path.exists("expense.json"):
    with open("expense.json","r") as file:
        expense = json.load(file)
else:
        expense = {"FOOD": "300", "ELECTRICITY": "400"}
       
total = 0 

expense.update({"House":"1000"})
expense.update({"FOOD":"500"})

for name,value in expense.items():
    print (f"{name} : ${value}")
    total += int(value)


print (f"total : ${total}")

with open("expense.json","w") as file:
    json.dump(expense, file, indent=4)
    print("Expense history has been updated!")
    