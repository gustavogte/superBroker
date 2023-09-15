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
        if usrname == False:
            input("\nPress any key to continue...")
            main()
        else:
            print(f"Welcome {usrname}!")
            with open(User.file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["usrname"] == usrname:
                        user = User(
                            row["usrname"],
                            row["password"],
                            row["email"],
                            row["phone"],
                        )
            print(f"Hola {user.usrname}!!!") 
    else:
        print("Thank you for visit SuperBroker\n")

    # account = Account()
    # print("Balance:", account.balance)
    # account.deposit(100)
    # account.withdraw(50)
    # print("Balance:", account.balance)


if __name__ == "__main__":
    main()
