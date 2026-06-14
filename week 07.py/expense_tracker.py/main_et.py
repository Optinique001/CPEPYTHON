# COMMAND LINE EXPENSE TRACKER

expenses = [
    [1, "05", "Data Subscription", 2500],
    [2, "06", "Lunch", 1200],
    [3, "06", "Transport", 800]
]
# ADD EXPENSE

def add_expense(month, description, amount):
    expense_id = len(expenses) + 1
    expenses.append([expense_id, month, description, amount])
    print("Expense added successfully!\n")

# VIEW ALL EXPENSES

def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\n===== ALL EXPENSES =====")

    for expense in expenses:
        print(
            f"ID: {expense[0]} | "
            f"Month: {expense[1]} | "
            f"Item: {expense[2]} | "
            f"Amount: ₦{expense[3]}"
        )

    print()

# UPDATE EXPENSE

def update_expense(expense_id, new_description, new_amount):

    for expense in expenses:

        if expense[0] == expense_id:
            expense[2] = new_description
            expense[3] = new_amount

            print("Expense updated successfully!\n")
            return

    print("Expense ID not found.\n")

# DELETE EXPENSE

def delete_expense(expense_id):

    for expense in expenses:

        if expense[0] == expense_id:
            expenses.remove(expense)

            print("Expense deleted successfully!\n")
            return

    print("Expense ID not found.\n")

# TOTAL SUMMARY

def summary_all():

    total = sum([expense[3] for expense in expenses])

    print(f"\nTotal Expenses: ₦{total}\n")

# MONTHLY SUMMARY

def summary_by_month(month):

    monthly_total = sum(
        [expense[3] for expense in expenses if expense[1] == month]
    )

    print(f"\nTotal expenses for month {month}: ₦{monthly_total}\n")

# MAIN PROGRAM

while True:

    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. View Total Summary")
    print("6. View Monthly Summary")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # ADD
    if choice == "1":

        month = input("Enter month (e.g 06): ")
        description = input("Enter description: ")
        amount = int(input("Enter amount: "))

        add_expense(month, description, amount)

    # VIEW
    elif choice == "2":
        view_expenses()

    # UPDATE
    elif choice == "3":

        expense_id = int(input("Enter expense ID: "))
        new_description = input("Enter new description: ")
        new_amount = int(input("Enter new amount: "))

        update_expense(expense_id, new_description, new_amount)

    # DELETE
    elif choice == "4":

        expense_id = int(input("Enter expense ID to delete: "))

        delete_expense(expense_id)

    # TOTAL SUMMARY
    elif choice == "5":
        summary_all()

    # MONTHLY SUMMARY
    elif choice == "6":

        month = input("Enter month: ")

        summary_by_month(month)

    # EXIT
    elif choice == "7":

        print("Program closed.")
        break

    else:
        print("Invalid choice.\n")
    
    # END OF PROGRAM