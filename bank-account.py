#import os module for terminal clearing
import os

"""
ACS-1111 Bank Account assignment
This code is written in Python and will simulate actions of a bank account
"""

class BankAccount: 
    """
    docstring
    """
    def __init__(self, full_name, account_number):
        """
        docstring
        """
        self.full_name = full_name
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        """
        docstring
        """
        if amount >= 0:
            self.balance += amount
            print(f"Amount deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print(f"Invalid deposit amount. Must enter a value greater than 0.")
        print()
    
    def withdraw(self, amount):
        """ 
        docstring
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
        docstring
        """
        print(f"Hi {self.full_name}, your current balance is: {self.balance:.2f}")
        print()
    
    def add_interest(self, monthly_interest_rate = 0.00083):
        """
        docstring
        """
        interest = self.balance * monthly_interest_rate
        self.balance += interest

    def print_statement(self):
        """
        docstring
        """
        print(f"{self.full_name}")
        print(f"Account No.: ****{self.account_number[4:len(self.account_number)]}")
        print(f"Balance: {self.balance:.2f}")
        print()

# Instantiating required bank accounts

mark_account = BankAccount("Mark Rattle", "08675309")
homer_account = BankAccount("Homer Simpson", "13371337")
mitchell_account = BankAccount("Mitchell Mitcherson", "03141592")

# Clear the terminal and run the required code to show class function

os.system('clear')

# Mitchell Mitcherson's account
mitchell_account.get_balance()
mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
# Mitch needs to buy some Yeezys
mitchell_account.withdraw(150)
mitchell_account.print_statement()

# Mark Rattle's account
mark_account.get_balance()
mark_account.deposit(1200)
mark_account.print_statement()
mark_account.add_interest()
mark_account.print_statement()
# Mark needs to buy a new Keychron Q2 Barebones kit
mark_account.withdraw(170)
mark_account.print_statement()

# Homer Simpson's account
homer_account.get_balance()
homer_account.deposit(60407)
homer_account.print_statement()
homer_account.add_interest()
homer_account.print_statement()
# Homer needs to buy some donuts and Duff beer
homer_account.withdraw(20)
homer_account.print_statement()