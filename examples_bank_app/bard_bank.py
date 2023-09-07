import csv
import hashlib
import secrets


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, name, balance):
        account = Account(name, balance)
        self.accounts[name] = account

    def get_account(self, name):
        return self.accounts[name]

    def deposit_to_account(self, name, amount):
        self.accounts[name].deposit(amount)

    def withdraw_from_account(self, name, amount):
        self.accounts[name].withdraw(amount)

    def get_balance_of_account(self, name):
        return self.accounts[name].get_balance()

    def save_data_to_csv(self, filename):
        with open(filename, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["name", "balance"])
            for name, account in self.accounts.items():
                writer.writerow([name, account.balance])


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = hashlib.sha256(
            password.encode() + secrets.token_hex(16).encode()
        ).hexdigest()

    def is_authenticated(self):
        return (
            self.password_hash
            == hashlib.sha256(
                input("Enter your password: ").encode() + secrets.token_hex(16).encode()
            ).hexdigest()
        )


class BankApp:
    def __init__(self):
        self.bank = Bank("My Bank")
        self.users = {}

    def create_user(self, name, email, password):
        user = User(name, email, password)
        self.users[name] = user

    def login(self):
        name = input("Enter your name: ")
        if name in self.users:
            user = self.users[name]
            if user.is_authenticated():
                print("Login successful!")
            else:
                print("Incorrect password.")
        else:
            print("User not found.")

    def sign_up(self):
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        self.create_user(name, email, password)
        print("Sign up successful!")

    def main(self):
        while True:
            print("1. Login")
            print("2. Sign up")
            print("3. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.login()
            elif choice == "2":
                self.sign_up()
            elif choice == "3":
                break


if __name__ == "__main__":
    app = BankApp()
    app.main()
