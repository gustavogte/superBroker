import os


class User:
    def __init__(self, name, password, email, phone):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone

    def __str__(self):
        return (
            "Name: "
            + self.name
            + "\nPassword: "
            + self.password
            + "\nEmail: "
            + self.email
            + "\nPhone: "
            + self.phone
        )

    def sign_up():
        print("Sign up")
        name = input("Name: ")
        password = input("Password: ")
        email = input("Email: ")
        phone = input("Phone: ")
        user = User(name, password, email, phone)
        return user

    def login():
        print("Login")
        user = input("user: ")
        password = input("password: ")
        print(f"Hello User: {user}")
