import csv
import os
from datetime import datetime

class Account:
    file_path = "data/account_data.csv"
    accounts = dict()
    account_num = 100

    def __init__(self, usrname, account_num, balance):
        self.usrname = usrname
        self.account_num = account_num
        self.balance = balance

        Account.account_num = Account.account_num + 1
        
    def __str__(self):
        return (
            "Username: "
            + self.usrname
            + " **** Account Number: "
            + str(self.account_num)
            + " **** Balance: "
            + str(self.balance)
        )

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

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
        print("Create account")
        account_usrname = usrname
        account_num = Account.account_num
        account_balance = 0
        account = cls(account_usrname, account_num, account_balance)
        print(f"Dear user: {account.usrname} your New Account is {account.account_num}. Starting balance = {account.balance}  ")
        cls.save_account(account)
        return account

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
    def check_account(cls, account):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["account_num"] == account:
                    return True
            return False
    
    @classmethod
    def save_transaction(cls):
        with open("transaction_data.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["account_num", "amount", "balance", "date"])
            writer.writerow({"account_no": cls.account_num, "amount": cls.amount, "balance": cls.balance, "date": datetime.now()})

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

def main():
    usrname = input("Whats your usrname: ")
    account = Account.create_account(usrname)
    print(account)
    usrname = input("Whats your usrname: ")
    account2 = Account.create_account(usrname) #class Method
    print(account2)
    #print(Account.account_num)
    #account3 = Account("Jenny", 3, 10) # instance
    #print(account3)
    account.deposit(50000)
    print(account)
    account.withdraw(500)
    print(account)
    account2.deposit(70000)
    account2.withdraw(2000)
    print(account2)
    




main()

