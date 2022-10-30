#import os module for terminal clearing
import os

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
    Output - none until methods are called
    """
    def __init__(self, full_name, account_number):
        """
        Class initialization
        """
        self.full_name = full_name
        self.account_number = account_number
        self.balance = 0

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
    
    def add_interest(self, monthly_interest_rate = 0.00083):
        """
        add_interest method is used to add interest to a balance at a predetermined interest rate.
        Required input - monthly_interest_rate (float), assigned default value of 0.00083 (0.083%).
        Output - string to indicate the interest accrued after one month.
        """
        interest = self.balance * monthly_interest_rate
        self.balance += interest
        print(f"The interest you've accrued for this statement period is: ${interest:.2f}")
        print()

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

# Instantiating required test bank accounts

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
print("="*20)

# Mark Rattle's account
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
homer_account.get_balance()
homer_account.deposit(60407)
homer_account.print_statement()
homer_account.add_interest()
homer_account.print_statement()
# Homer needs to buy some donuts and Duff beer
homer_account.withdraw(20)
homer_account.print_statement()
print("="*20)