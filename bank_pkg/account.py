import csv
import os
from datetime import datetime


class Account:
    file_path = "./data/account_data.csv"
    accounts = list()
    account_num = 100

    def __init__(self, usrname, account_num, balance):
        self.usrname = usrname
        # self.account_num = Account.get_last_account() + 1
        self.account_num = account_num
        self.balance = balance

    def __str__(self):
        return (
            "Username: "
            + self.usrname
            + " **** Account Number: "
            + str(self.account_num)
            + " **** Balance: "
            + str(self.balance)
        )

    def check_balance(self):
        print(f"Your balance is: ${self.balance:,.2f}")

    def deposit(self, amount):
        Account.check_amount(amount)
        self.balance += int(amount)
        Account.update_balance(self.account_num, self.balance)

    def withdraw(self, amount):
        Account.check_amount(amount)
        self.balance -= int(amount)
        Account.update_balance(self.account_num, self.balance)

    # this is a getter
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        try:
            int(balance)
        except (ValueError):
            raise ValueError("Balance must be an number")
        if int(balance) < 0:
            raise ValueError("Account balance to not suffcient for this operation")
        self._balance = int(balance)

    @classmethod
    def check_amount(self, amount):
        try:
            int(amount)
        except (ValueError):
            raise ValueError("Amount must be an number")
        if int(amount) < 0:
            raise ValueError("Amount must be greater than 0")
        else:
            return int(amount)

    @classmethod
    def initialize_csv(cls):
        if not os.path.exists(cls.file_path):
            with open(cls.file_path, "w", newline="") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["usrname", "account_num", "balance"]
                )
                writer.writeheader()

    @classmethod
    def create_account(cls, usrname):
        print("\nSet up account:")
        account_usrname = usrname
        account_num = Account.get_last_account() + 1
        account_balance = 0
        account = cls(account_usrname, account_num, account_balance)
        print(
            f"\nDear user: *** {account.usrname} *** your New Account is *** {account.account_num} ***. Starting balance = ${account.balance:,.2f}  "
        )
        cls.save_account(account)
        return account

    @classmethod
    def get_last_account(cls):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Account.accounts.append(int(row["account_num"]))
            try:
                return max(Account.accounts)
            except (ValueError):
                return 100

    @classmethod
    def save_account(cls, account):
        with open(cls.file_path, "a", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["usrname", "account_num", "balance"]
            )
            writer.writerow(
                {
                    "usrname": account.usrname,
                    "account_num": account.account_num,
                    "balance": account.balance,
                }
            )

    @classmethod
    def get_account(cls, usrname):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["usrname"] == usrname:
                    account = Account(
                        row["usrname"], row["account_num"], row["balance"]
                    )
                    return account

    @classmethod
    def check_account(cls, account):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["account_num"] == account:
                    return True
            return False

    @classmethod # You have to overwrite file
    def update_balance(cls, account_num, new_balance):
        input_file = cls.file_path
        output_file = "./data/modified.csv"
        with open(input_file, "r") as csvfile, open(output_file, "w", newline="") as modified_csvfile:
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(modified_csvfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if row["account_num"] == account_num:
                    row["balance"] = new_balance
                writer.writerow(row)
        os.remove(input_file)
        os.rename(output_file, input_file)
        return True

    @classmethod
    def save_transaction(cls):
        with open("../data/transaction_data.csv", "a", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["account_num", "amount", "balance", "date"]
            )
            writer.writerow(
                {
                    "account_num": cls.account_num,
                    "amount": cls.amount,
                    "balance": cls.balance,
                    "date": datetime.now(),
                }
            )

Account.initialize_csv()
