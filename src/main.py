import utils

def main():
    while True:
        try: 
            ures = int(input("===== Expense Tracker =====\n\n1. Add Expense\n2. Show Expenses\n3. Show Total\n4. Search Expense\n5. Delete Expense\n6. Summery expense\n7. Exit\n\nSelect : "))    
            
            if ures == 7:
                print("Thank you for using Expense Tracker")
                break
                
            elif ures == 1:
                utils.add_expense(ures)
            elif ures == 2:
                utils.show_expenses(ures)
            elif ures == 3:
                utils.calculate_total(ures)
            elif ures == 4:
                utils.search_expense(ures)
            elif ures == 5:
                utils.delete_expense(ures)
            elif ures == 6:
                utils.summery_expense(ures)
            else:
                print("\n[!] Invalid option number. Please try again.\n")
                
        except ValueError:
            print("\n[!] Error: Please enter a valid number, not text.\n")
            

if __name__ == "__main__":
    main()