# Core Banking System Simulator

## Project Overview

This project is a simple Core Banking System Simulator built with Python using Object-Oriented Programming (OOP) and File Handling.

The program allows users to create bank accounts, deposit money, withdraw money, check account balances, and save account information even after the program is closed.

The goal of this project was to practice important Python concepts such as inheritance, method overriding, classes, objects, and JSON file handling.

---

## Features

* Open a Savings Account
* Open a Current Account
* Deposit Money
* Withdraw Money
* Check Account Balance
* Add Interest to Savings Accounts
* Save Account Data to a JSON File
* Load Existing Account Data Automatically

---

## OOP Concepts Used

### Parent Class

The `BankAccount` class serves as the parent class and contains common attributes and methods shared by all account types.

Attributes:

* Account Number
* Account Holder
* Balance

Methods:

* Deposit
* Withdraw
* Get Balance

### Child Classes

#### SavingsAccount

The `SavingsAccount` class inherits from `BankAccount`.

Additional Features:

* Maintains a minimum balance of ₦1000.
* Prevents withdrawals that would reduce the balance below ₦1000.
* Supports adding interest to the account.

#### CurrentAccount

The `CurrentAccount` class inherits from `BankAccount`.

Additional Features:

* Supports overdraft.
* Allows withdrawals beyond the current balance up to a specified overdraft limit.

---

## File Handling

This project uses a JSON file called `bank_data.json` to store account information.

Functions Used:

### save_data()

Converts account objects into dictionaries and saves them to a JSON file.

### load_data()

Loads saved account information from the JSON file when the program starts and recreates the account objects.

This ensures that account data is not lost when the program closes.

---

## Menu Options

1. Open New Account
2. Deposit
3. Withdraw
4. Check Balance
5. Add Interest (Savings Account)
6. Exit

Selecting Exit automatically saves all account data.

---

## What I Learned

Through this project, I learned:

* How inheritance reduces code repetition.
* How method overriding allows different account types to behave differently.
* How to store and retrieve data using JSON files.
* How to build a menu-driven application.
* How Object-Oriented Programming can be used to model real-world systems.

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON
* File Handling

---

## Author

Paul Nnaemeka

Computer Engineering Student

This project was developed as part of my OOP and File Handling practice to strengthen my understanding of Python software development.
