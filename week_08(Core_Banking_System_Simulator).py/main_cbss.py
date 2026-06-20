import json
import os

# Parent Class

class BankAccount:

    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₦{amount:,.2f} deposited successfully.")

    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance


# Savings Account

class SavingsAccount(BankAccount):
    min_balance = 1000

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("Transaction declined! Minimum balance must remain ₦1000.")
        else:
            self.balance -= amount
            print(f"₦{amount:,.2f} withdrawn successfully.")

    def add_interest(self, rate):
        interest = self.balance * (rate / 100)
        self.balance += interest
        print(f"Interest added: ₦{interest:,.2f}")


# Current Account

class CurrentAccount(BankAccount):

    def __init__(self, account_number, account_holder,
                 balance=0, overdraft_limit=10000):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            print("Transaction declined! Overdraft limit exceeded.")
        else:
            self.balance -= amount
            print(f"₦{amount:,.2f} withdrawn successfully.")


# Save Data

def save_data(accounts):
    data = []

    for acc in accounts:
        if isinstance(acc, SavingsAccount):
            account_type = "Savings"

            data.append({
                "type": account_type,
                "account_number": acc.account_number,
                "account_holder": acc.account_holder,
                "balance": acc.balance
            })

        elif isinstance(acc, CurrentAccount):
            account_type = "Current"

            data.append({
                "type": account_type,
                "account_number": acc.account_number,
                "account_holder": acc.account_holder,
                "balance": acc.balance,
                "overdraft_limit": acc.overdraft_limit
            })

    with open("bank_data.json", "w") as file:
        json.dump(data, file, indent=4)


# Load Data

def load_data():
    accounts = []

    if not os.path.exists("bank_data.json"):
        return accounts

    with open("bank_data.json", "r") as file:
        data = json.load(file)

    for item in data:

        if item["type"] == "Savings":
            acc = SavingsAccount(
                item["account_number"],
                item["account_holder"],
                item["balance"]
            )

        elif item["type"] == "Current":
            acc = CurrentAccount(
                item["account_number"],
                item["account_holder"],
                item["balance"],
                item["overdraft_limit"]
            )

        accounts.append(acc)

    return accounts


# Find Account

def find_account(accounts, acc_no):
    for account in accounts:
        if account.account_number == acc_no:
            return account
    return None


# Main Program

accounts = load_data()

while True:

    print("\n=== CORE BANKING SYSTEM ===")
    print("1. Open New Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Add Interest (Savings Account)")
    print("6. Exit")

    choice = input("Enter choice: ")

    # Open Account

    if choice == "1":

        acc_no = input("Account Number: ")
        holder = input("Account Holder Name: ")

        print("\n1. Savings Account")
        print("2. Current Account")

        acc_type = input("Select account type: ")

        if acc_type == "1":
            account = SavingsAccount(acc_no, holder)
            accounts.append(account)

        elif acc_type == "2":
            overdraft = float(input("Overdraft Limit: "))
            account = CurrentAccount(
                acc_no,
                holder,
                overdraft_limit=overdraft
            )
            accounts.append(account)

        else:
            print("Invalid account type.")
            continue

        print("Account created successfully!")

    # Deposit

    elif choice == "2":

        acc_no = input("Account Number: ")
        account = find_account(accounts, acc_no)

        if account:
            amount = float(input("Amount: "))
            account.deposit(amount)
        else:
            print("Account not found.")

    # Withdraw

    elif choice == "3":

        acc_no = input("Account Number: ")
        account = find_account(accounts, acc_no)

        if account:
            amount = float(input("Amount: "))
            account.withdraw(amount)
        else:
            print("Account not found.")

    # Check Balance

    elif choice == "4":

        acc_no = input("Account Number: ")
        account = find_account(accounts, acc_no)

        if account:
            print(f"Current Balance: ₦{account.get_balance():,.2f}")
        else:
            print("Account not found.")

    # Add Interest

    elif choice == "5":

        acc_no = input("Account Number: ")
        account = find_account(accounts, acc_no)

        if isinstance(account, SavingsAccount):
            rate = float(input("Interest Rate (%): "))
            account.add_interest(rate)

        elif account:
            print("Interest can only be added to a Savings Account.")

        else:
            print("Account not found.")

    # Exit

    elif choice == "6":
        save_data(accounts)
        print("Data saved successfully.\n")
        print("Exiting...")
        break

    else:
        print("Invalid choice.")