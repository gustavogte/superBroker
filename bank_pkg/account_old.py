import csv
import os
from datetime import datetime

class Account:
    file_path = "account_data.csv"

    def __init__(self, usrname, account_num, balance):
        self.usrname = usrname
        self.account_num = account_num 
        self.balance = balance

    def __str__(self):
        return (
            "Username: "
            + self.usrname
            + " Account Number: "
            + self.account_no
            + " Balance: "
            + self.balance
        )

    # this is a getter
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    @balance.setter
    def balance(self, value):
        self._balance = value

    @classmethod
    def initialize_csv(cls):
        if not os.path.exists(cls.file_path):
            with open(cls.file_path, "w", newline="") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["usrname", "account_no", "balance"]
                )
                writer.writeheader()

    @classmethod
    def create_account(cls):
        print("Add accounts")
        account_type = input("Account type: ")
        account_num = input("Account number: ")
        account_balance = input("Account balance: ")
        account_currency = input("Account currency: ")
        account_status = input("Account status: ")
        account = cls(account_type, account_num, account_balance, account_currency, account_status)
        cls.save_accounts(account)
        return account

    @classmethod
    def save_account(cls, account):
        with open(cls.file_path, "a", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["account_type", "account_num",   "account_balance", "account_currency", "account_status"]
            )
            writer.writerow(
                {
                    "acc_type": account.account_type,
                    "acc_num": account.account_num,
                    "acc_balance": account.account_balance,
                    "acc_currency": account.account_currency,
                    "acc_status": account.account_status,
             }
            )

    @classmethod
    def check_account(cls, account):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["account_no"] == account:
                    return True
            return False
    
    @classmethod
    def save_transaction(cls):
        with open("transaction_data.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["account_no", "amount", "balance", "date"])
            writer.writerow({"account_no": cls.account, "amount": cls.amount, "balance": cls.balance, "date": datetime.now()})

    @classmethod
    def get_balance(cls, account):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["account_no"] == account:
                    return row["balance"]
            return False
        
    @classmethod
    def get_usr(cls, account):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["account_no"] == account:
                    return row["usrname"]
            return False
    
    @classmethod
    def get_account(cls, usr):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["usrname"] == usr:
                    return row["account_no"]
            return False
        
    @classmethod
    def get_all_accounts(cls):
        accounts = []
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts.append(row["account_no"])
            return accounts
    
    @classmethod
    def get_all_accounts_with_balance(cls):
        accounts = []
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts.append([row["account_no"], row["balance"]])
            return accounts
    
    @classmethod
    def get_all_accounts_with_usr(cls):
        accounts = []
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts.append([row["account_no"], row["usrname"]])
            return accounts
    
    @classmethod
    def get_all_accounts_with_usr_balance(cls):
        accounts = []
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts.append([row["account_no"], row["usrname"], row["balance"]])
            return accounts
    
Account.initialize_csv()
