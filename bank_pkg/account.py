import csv
import os
from datetime import datetime

class Account:
    file_path = "./data/account_data.csv"
    accounts = list()
    account_num = 100

    def __init__(self, usrname, account_num, balance):
        self.usrname = usrname
        #self.account_num = Account.get_last_account() + 1 
        self.account_num = account_num
        self.balance = int(balance)
        
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
        self.balance += amount
        Account.update_balance(self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        Account.update_balance(self.balance)

    # this is a getter
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        self._balance = value

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
        print(f"\nDear user: *** {account.usrname} *** your New Account is *** {account.account_num} ***. Starting balance = ${account.balance:,.2f}  ")
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
                file, fieldnames=["usrname", "account_num","balance"]
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
                        row["usrname"],
                        row["account_num"], 
                        row["balance"])
                    return account

    @classmethod
    def check_account(cls, account):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["account_num"] == account:
                    return True
            return False
    
    @classmethod
    def update_balance(cls, new_balance):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["account_num"] == cls.account_num:
                    row["balance"] = new_balance
                    print("hello")
                    wait = input("Wait key ....")
                    writer = csv.DictWriter(file, fieldnames=["usrname","account_num", "balance"])
                    writer.writerow({
                        "balance" : new_balance
                    })
            return False

    @classmethod
    def save_transaction(cls):
        with open("../data/transaction_data.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["account_num", "amount", "balance", "date"])
            writer.writerow({"account_num": cls.account_num, "amount": cls.amount, "balance": cls.balance, "date": datetime.now()})

    
Account.initialize_csv()
