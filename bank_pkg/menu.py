import os

def menu_1():
    while True:
        os.system("clear")
        print("Welcome to SuperBroker\n")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit\n")
        try:
            selection = int(input("Enter your choice: "))
            if selection > 0 and selection < 4:
                os.system("clear")
                return selection
            else:
                True
        except ValueError:
            True

def menu_2(user, account):
    while True:
        os.system("clear")
        print(f"Welcome to SuperBroker {user.usrname}!\n")
        print(f"Account Number: {account.account_num}\n")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit\n")
        try:
            selection2 = int(input("Enter your choice: "))
            if selection2 > 0 and selection2 < 5:
                os.system("clear")
                return selection2
            else:
                True
        except ValueError:
            True

    