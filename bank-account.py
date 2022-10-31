#import os module for terminal clearing
import os
#import randint for random numbers
from random import randint
#import re for regular expression matching
import re

"""
ACS-1111 Bank Account assignment
This code is written in Python and will simulate actions of a bank account
"""

class BankAccount: 
    """
    BankAccount class is called to instantiate new BankAccount objects that initialize with a full name,
    and account number as required parameters, and a pre-assigned starting balance of 0
    Input params -  full_name (string) - Full name of account owner
                    account_number (string) - Account number associated with the account
                    account_type (string) - Account type, either checking or savings & defaults to checking
    Output - none until methods are called
    """
    def __init__(self, full_name, account_number, account_type = 'checking'):
        """
        Class initialization
        """
        self.full_name = full_name
        self.account_number = account_number
        self.balance = 0
        self.account_type = account_type

    def deposit(self, amount):
        """
        Deposit method is used to deposit money into a user's account
        Input - amount (float), amount to be deposited. Must be > 0.
        Output - updates balance and prints strings to confirm a deposit
        """
        if amount >= 0:
            self.balance += amount
            print(f"Amount deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print(f"Invalid deposit amount. Must enter a value greater than 0.")
        print()
    
    def withdraw(self, amount):
        """ 
        Withdraw method is used to withdraw money into a user's account.  Charges a NSF of $10 if there is insufficient balance
        Input - amount (float), amount to be withdrawn. Must be > 0.
        Output - updates balance and prints strings to confirm a withdrawal or insufficient balance
        """
        if amount >= 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Amount withdrawn: ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print(f"Insufficient funds.  The maximum that you can withdraw is ${self.balance:.2f}")
                self.balance -= 10
                print(f"You have been charged an overdraft fee of $10.00. Your current remaining value is: ${self.balance:.2f}")                
        else:
            print(f"Invalid withdrawal amount. Must enter a value greater than 0.")
        print()

    def get_balance(self):
        """
        Get_balance method is used to display a friendly greeting and the current balance of an account.
        Required input - none (self only)
        Output - string to greet full_name & self.balance.
        """
        print(f"Hi {self.full_name}, your current balance is: ${self.balance:.2f}")
        print()
        return self.balance
    
    def add_interest(self):
        """
        add_interest method is used to add interest to a balance at a predetermined interest rate for account type.
        Required input - account_type (string) - determines the monthly interest (0.083% for checking, 0.1% for savings).
        Output - returns the interest accrued for the month and prints a string to confirm.
        """
        print(f"{self.full_name}, your pre-interest balance is: ${self.balance:.2f}")
        print()
        if self.account_type == "savings":
            monthly_interest_rate = 0.001
        else:
            monthly_interest_rate = 0.00083
        interest = self.balance * monthly_interest_rate
        self.balance += interest
        print(f"The interest you've accrued for this statement period in your {self.account_type} account is: ${interest:.2f}")
        print()
        return interest

    def print_statement(self):
        """
        print_statement method is used to print a full statement of current account information.
        Required input - None (self only)
        Output - string with name, account number and balance of the current account
        """
        print(f"{self.full_name}")
        print(f"Account No.: ****{self.account_number[4:len(self.account_number)]}")
        print(f"Balance: ${self.balance:.2f}")
        print()

# allow customization of account number length, must be an int. 
# Written so that it could take user input if desired but currently uses a preassigned value

account_number_length = 8
def generate_account_number(account_number_length):
    """
    generate_account_number function is used to randomly generate an account number of length account_number_length.
    Required input - account_number_length (int) - number of digits in the account number
    Output - returns an account_number as a string
    """
    i = 0
    account_number = ''
    while i < account_number_length:
        account_number += str(randint(0,9))
        i += 1
    return account_number

# Define an empty list called "bank" to append new accounts to
bank = []

# Instantiating required test bank accounts with account number as a randomly generated 8 digit string
mark_account = BankAccount("Mark Rattle", generate_account_number(account_number_length),"checking")
bank.append(mark_account)
homer_account = BankAccount("Homer Simpson", generate_account_number(account_number_length),"savings")
bank.append(homer_account)
mitchell_account = BankAccount("Mitchell Mitcherson", generate_account_number(account_number_length),"checking")
bank.append(mitchell_account)

def demonstration ():
    """
    demonstration function is used to print out pre.
    Required input - account_number_length (int) - number of digits in the account number
    Output - returns an account_number as a string
    """
# Clear the terminal and run the required code to show class function

    os.system('clear')

# Mark Rattle's account
    print("Demo for Mark Rattle's account:")
    print()
    mark_account.get_balance()
    mark_account.deposit(1200)
    mark_account.print_statement()
    mark_account.add_interest()
    mark_account.print_statement()
    # Mark needs to buy a new Keychron Q2 Barebones kit
    mark_account.withdraw(170)
    mark_account.print_statement()
    print("="*20)

# Homer Simpson's account
    print("Demo for Homer Simpson's account:")
    print()
    homer_account.get_balance()
    homer_account.deposit(1200)
    homer_account.print_statement()
    homer_account.add_interest()
    homer_account.print_statement()
    # Homer needs to buy some donuts and Duff beer
    homer_account.withdraw(20)
    homer_account.print_statement()
    print("="*20)

# Mitchell Mitcherson's account
    print("Demo for Mitchell Mitcherson's account:")
    print()
    mitchell_account.get_balance()
    mitchell_account.deposit(400000)
    mitchell_account.print_statement()
    mitchell_account.add_interest()
    mitchell_account.print_statement()
    # Mitch needs to buy some Yeezys
    mitchell_account.withdraw(150)
    mitchell_account.print_statement()
    print("="*20)

# Add one month of interest for each account in the bank list and print a new statement

    for account in bank:
        print(f"Adding one month of interest to {account.full_name}'s {account.account_type} account...")
        print()
        account.add_interest()
        account.print_statement()
        print("=" * 20)

os.system('clear')
print ("Welcome to Mark's Bank!")
input("The demonstration showing required code will now run. \33[32mPlease press ENTER to continue.\33[0m")
demonstration()

# Run program in a loop after showing the demo output
program_loop = True

while program_loop == True:
    i = 0
    account_choice = ""
    account_choice_list = []
    print ("Please select an account:")
    for account in bank:
        i += 1
        account_choice_list.append(str(i))
        print (f"Account {i} - {account.full_name}")
    account_choice = input("Enter your choice as a number from the list above > ")
    while account_choice not in account_choice_list:
        account_choice = input("Invalid entry, please enter a number from the list above > ")
        while not re.match("[0-9]", account_choice):
            account_choice = input("Invalid entry, please enter a number from the list above > ")
    print(":)")    


