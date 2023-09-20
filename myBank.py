from bank_pkg import Account
from bank_pkg import menu_1, menu_2
from bank_pkg import User
import csv


def main():
    selection = menu_1()
    if selection == 1:
        user = User.sign_up()
        print(f"\nWelcome to SuperBroker {user.usrname}!")
        input("\nPress any key to continue...")
        main()
    elif selection == 2:
        usrname = User.login()
        if usrname:
            user = User.get_user(usrname)
            account = Account.get_account(usrname)
            print(f"Welcome {user.usrname}!!")
            print(f"\nAccount Number: {account.account_num}")

            input("\nPress any key to continue...")
        else:
            input("\nPress any key to continue...")
            main()
    else:
        print("Thank you for visit SuperBroker\n")

if __name__ == "__main__":
    main()
