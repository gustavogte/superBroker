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


def menu_2():
    pass

    
