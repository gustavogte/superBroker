from bank_pkg.account import Account
from bank_pkg import menu_1, menu_2
from bank_pkg import User


def main():
    selection = menu_1()
    if selection == 1:
        user = User.sign_up()
        print(f"Welcome {user.name}")
        input("Press any key to continue...")
        users = list()
        print(type(users))
        users = users.append(user)
        print(users)
        input("Press any key to continue...")
        main()
    elif selection == 2:
        user = User.login()
    else:
        print("Thank you for visit SuperBroker\n")

    # account = Account()
    # print("Balance:", account.balance)
    # account.deposit(100)
    # account.withdraw(50)
    # print("Balance:", account.balance)


if __name__ == "__main__":
    main()
