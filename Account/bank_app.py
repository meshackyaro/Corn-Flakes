from Account.InsufficientFundsError import InsufficientFundsError
from Account.InvalidAmountError import InvalidAmountError
from Account.InvalidPinError import InvalidPinError
from Account.bank import Bank


class BankApp:
    def __init__(self):
        self.bank = Bank("Mavericks")

    def display(self):
        print('Welcome To Mavericks Bank App')
        print('What would you like to do?')
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
        print('1. Open Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Close Account\n7. Exit')
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

        option = input('Select option: ')

        if option == '1':
            self.create_account()
        elif option == '2':
            self.check_balance()
        elif option == '3':
            self.deposit()
        elif option == '4':
            self.withdraw()
        elif option == '5':
            self.transfer()
        elif option == '6':
            self.close_account()
        elif option == '7':
            self.exit()
        else:
            print('Enter a correct option from 1 to 7')
            self.display()

    def create_account(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        pin = input('Enter new PIN: ')
        account = self.bank.register_customer(first_name, last_name, pin)
        print("\nCongratulations! You're now a Maverick")
        print('Your new account number is: ', account.get_number(), '\n\n')
        self.display()

    def check_balance(self):
        account_number = input('Enter account number:')
        pin = input('Enter PIN: ')
        try:
            balance = self.bank.check_balance(int(account_number), pin)
            print('Your account balance is: ' '#', balance)
        except InvalidPinError as e:
            print(e)
        finally:
            self.display()

    def deposit(self):
        account_number = input('Enter account number: ')
        amount = input('Enter amount: ')
        try:
            self.bank.deposit(int(account_number), int(amount))
            print('Amount deposited successfully')
        except InvalidAmountError as e:
            print(e)
        finally:
            self.display()

    def withdraw(self):
        account_number = input('Enter account number: ')
        amount = input('Enter amount: ')
        pin = input('Enter PIN: ')
        try:
            self.bank.withdraw(int(account_number), int(amount), pin)
            print('Amount withdrawn successfully')
        except InsufficientFundsError as e:
            print(e)
        except InvalidPinError as e:
            print(e)
        finally:
            self.display()

    def transfer(self):
        sender_account = input("Enter sender's account number: ")
        recipient_account = input("Enter recipient's account number: ")
        amount = input('Enter amount: ')
        pin = input('Enter PIN: ')
        try:
            self.bank.transfer(int(sender_account), int(recipient_account), int(amount), pin)
            print('Amount transferred successfully')
        except InsufficientFundsError as e:
            print(e)
        except InvalidAmountError as e:
            print(e)
        except InvalidPinError as e:
            print(e)
        finally:
            self.display()

    def close_account(self):
        account_number = input('Enter account number: ')
        pin = input('enter pin: ')
        try:
            self.bank.remove_account(account_number, pin)
            print('Account closed successfully')
        except InvalidPinError as e:
            print(e)
        finally:
            self.display()

    @staticmethod
    def exit():
        print('Exit')
        return


def main():
    bank_app = BankApp()
    bank_app.display()


if __name__ == "__main__":
    main()
