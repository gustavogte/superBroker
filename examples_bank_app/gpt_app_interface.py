from gpt_bank import Bank


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Simple Bank App!")
        print("1. Sign up")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            username = input("\nEnter your desired username: ")
            password = input("Enter your desired password: ")
            bank.sign_up(username, password)
            print("Successfully signed up!")
        elif choice == "2":
            username = input("\nEnter your username: ")
            password = input("Enter your password: ")
            is_logged_in, balance = bank.login(username, password)
            if is_logged_in:
                print(f"Logged in successfully! Your current balance is: ${balance}")
            else:
                print("Incorrect username or password!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
