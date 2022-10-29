"""
ACS-1111 Bank Account assignment
"""

class BankAccount: 

    def __init__(self, full_name, account_number):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = 0

    def deposit(amount):
        self.balance += amount
    
    def withdraw(amount):
        self.balance -= amount

    def get_balance():
        print(f"Hi {self.full_name}, balance is: {self.balance:.2f}")
    
    def add_interest(monthly_interest_rate = 0.00083):
        interest = balance * monthly_interest_rate
        balance += interest