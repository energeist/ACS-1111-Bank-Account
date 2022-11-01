# ACS-1111-Bank-Account
## Bank Account project for ACS1111
Written in Python (version 3.10)
## Project Description
This project is a simple app written to simulate banking actions on a set of pre-defined accounts.
Functionality includes:
- Randomized account numbers upon BankAccount object instantiation.  Uses a fix routing number which is identical for all accounts (becasue we all bank at the same branch!)
- Greeting the user
- Making a deposit for which the amount is validated
- Making a withdrawal for which the amount is validated, and charges NSF if the user does not have enough money in their account
- Accruing monthly interest at a rate according to account type: 
    1. 0.1% monthly for a savings account
    2. 0.083% monthly for a checking account
- Storing accounts in a 'bank' list for later recall

## Running this program
The program will initialize and display demo runs that show functionality as required by the project description.  Balances are then reinitialized to zero so that the user can take over and command the program from a fresh starting point.  The user can select an account to perform actions on and then loop within that account until they are finished and select another, if they choose to.  The program will exit when the user has indicated that they're finished.

