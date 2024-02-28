from Account.InsufficientFundsError import InsufficientFundsError
from Account.InvalidAmountError import InvalidAmountError
from Account.InvalidPinError import InvalidPinError


class Account:

    def __init__(self, name, pin, number):
        self.name = name
        self.balance = 0
        self.pin = pin
        self.number = number

    def check_balance(self, pin):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountError('Invalid Amount')
        self.balance += amount

    def withdraw(self, amount, pin):
        self.insufficient_funds(amount)
        self.invalid_amount(amount)
        self.validate(pin)
        self.balance -= amount

    def validate(self, pin):
        if not pin == self.pin:
            raise InvalidPinError('Invalid Pin')

    def invalid_amount(self, amount):
        if amount == 0:
            raise InvalidAmountError('Invalid Amount')

    def insufficient_funds(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError('Insufficient Funds')

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_balance(self):
        return self.balance
