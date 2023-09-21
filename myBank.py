from bank_pkg import Account
from bank_pkg import menu_1, menu_2
from bank_pkg import User


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
            login = True
            user = User.get_user(usrname)
            account = Account.get_account(usrname)
            while login == True:
                selection2 = menu_2(user, account)
                if selection2 == 1:
                    amount = input(f"Enter your deposit {user.usrname} to account {account.account_num}: ")
                    print("")
                    ok = True
                    while ok == True :
                        try:
                            account.deposit(amount)
                        except ValueError as err:
                            print(err)
                        ok = False
                    Account.check_balance(account)
                    input("\nPress any key to continue...")
                    #menu_2(user, account)
                elif selection2 == 2:
                    amount = input(f"How much do you want to withdraw {user.usrname} from account {account.account_num}: ")
                    print("")
                    ok = True
                    while ok == True :
                        try:
                            account.withdraw(amount)
                        except ValueError as err:
                            print(err)
                        ok = False
                    Account.check_balance(account)
                    input("\nPress any key to continue...")
                    #menu_2(user, account)
                elif selection2 == 3:
                    print(f"User: {user.usrname}  Account: {account.account_num}\n")
                    Account.check_balance(account)
                    input("\nPress any key to continue...")
                    #menu_2(user, account)            
                else:
                    print(f"Thank you for visit SuperBroker {user.usrname}!!!\n")
                    input("\nPress any key to continue...")
                    login = False
                    main()
        else:
            input("Press any key to continue ...")
    else:
        print("Thank you for visit SuperBroker\n")

if __name__ == "__main__":
    main()
