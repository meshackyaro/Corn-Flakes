from Account.InvalidAmountError import InvalidAmountError
from Account.InvalidPinError import InvalidPinError
from Account.account import Account


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.account_number = 0

    def register_customer(self, first_name, last_name, pin):
        account_number = self.generate_account_number()
        new_account = Account(first_name + " " + last_name, pin, account_number)
        self.accounts.append(new_account)
        return new_account

    def generate_account_number(self):
        self.account_number += 1
        return self.account_number

    def get_account(self):
        return len(self.accounts)

    def find_account(self, account_number):
        for new_account in self.accounts:
            if new_account.number == account_number:
                return new_account

    def deposit(self, number, amount):
        account = self.find_account(number)
        account.deposit(amount)

    def withdraw(self, number, amount, pin):
        account = self.find_account(number)
        account.withdraw(amount, pin)

    def check_balance(self, number, pin):
        account = self.find_account(number)
        return account.check_balance(pin)

    def remove_account(self, number, pin):
        account = self.find_account(number)
        if account.pin == pin:
            self.accounts.remove(account)
        else:
            raise InvalidPinError('Incorrect pin')

    def transfer(self, number, number1, amount, pin):
        sender = self.find_account(number)
        recipient = self.find_account(number1)
        sender.withdraw(amount, pin)
        recipient.deposit(amount)
