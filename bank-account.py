"""
ACS-1111 Bank Account assignment
"""

class BankAccount: 

    def __init__(self, full_name, account_number):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        print(f"Hi {self.full_name}, balance is: {self.balance:.2f}")
    
    def add_interest(monthly_interest_rate = 0.00083):
        interest = balance * monthly_interest_rate
        balance += interest

    def print_statement(self):
        print(f"{self.full_name}")
        print(f"Account No.: ****{self.account_number[4:len(self.account_number)]}")
        print(f"Balance: {self.balance}")

# mark_account = BankAccount(full_name, account_number)
# homer_account = BankAccount(full_name, account_number)
mitchell_account = BankAccount("Mitchell Mitcherson", "03141592")

mitchell_account.print_statement()


