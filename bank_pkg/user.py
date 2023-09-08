import csv
import os
import hashlib
import secrets  # to generate a secure random salt
import datetime


class User:
    users = []
    file_path = "user_data.csv"

    def __init__(self, usrname, password, email, phone):
        self.usrname = usrname
        self.password = password
        self.email = email
        self.phone = phone

    def __str__(self):
        return (
            "User Name: "
            + self.usrname
            + " Password: "
            + "********"  # self.password
            + " Email: "
            + self.email
            + " Phone: "
            + self.phone
        )

    @classmethod
    def initialize_csv(cls):
        if not os.path.exists(cls.file_path):
            with open(cls.file_path, "w", newline="") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["usrname", "password", "email", "phone"]
                )
                writer.writeheader()

    @classmethod
    def sign_up(cls):
        print("Sign up")
        usrname = input("User Name: ")
        password = input("Password: ")
        email = input("Email: ")
        phone = input("Phone: ")
        try:
            user = cls(usrname, password, email, phone)
            return user
        except ValueError as err:
            print(err)
            return User.sign_up()  # tal vez esto hay que dejarlo fuera de la función.

    @classmethod
    def save_user(cls, usr):
        with open(cls.file_path, "a", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["usrname", "password", "email", "phone"]
            )
            writer.writerow(
                {
                    "usrname": usr.usrname,
                    "password": usr.password,
                    "email": usr.email,
                    "phone": usr.phone,
                }
            )

    # Getter => @property
    # _ use for the function not to colide with the variable
    # _name is a private variable (honor system, not forced)
    @property
    def usrname(self):
        return self._usrname

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def phone(self):
        return self._phone

    # Setter => @x.setter
    @usrname.setter
    def usrname(self, usrname):
        if not usrname:
            raise ValueError("Missing name")
        self._usrname = usrname

    @email.setter
    def email(self, email):
        if "@" not in email:
            raise ValueError("Invalid email")
        self._email = email

    @password.setter
    def password(self, password):
        if not password:
            raise ValueError("Missing password")
        self._password = password

    @phone.setter
    def phone(self, phone):
        if not phone:
            raise ValueError("Missing phone")
        self._phone = phone

    def login():
        print("Login")
        user_name = input("user: ")
        password = input("password: ")
        print(f"Hello User: {user_name}")


def main():
    usr = User.sign_up()
    print(usr)
    User.initialize_csv()
    User.save_user(usr)
    print(User.users)


main()
