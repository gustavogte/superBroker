import csv
import os
import hashlib # is better to install bcrypt library
import secrets  # to generate a secure random salt
import datetime


class User:
    users = []
    file_path = "user_data.csv"

    @classmethod
    def initialize_csv(cls):
        if not os.path.exists(cls.file_path):
            with open(cls.file_path, "w", newline="") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["usrname", "hashed_password", "salt", "email", "phone"]
                )
                writer.writeheader()

    @classmethod
    def hash_password(cls, password, salt=None):
        if not salt:
            salt = secrets.token_hex(16)
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return password_hash, salt

    @classmethod
    def check_password(cls, username, password):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["usrname"] == username:
                    return cls.hash_password(password, row["salt"])[0] == row["hashed_password"]

    @classmethod
    def check_usr(cls, user):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["usrname"] == user:
                    return True
            return False

    @classmethod
    def sign_up(cls):
        cls.initialize_csv
        print("Sign up")
        usrname = input("User Name: ")
        password = input("Password: ")
        hashed_password = cls.hash_password(password)[0]
        salt = cls.hash_password(password)[1]
        email = input("Email: ")
        phone = input("Phone: ")
        try:
            user = cls(usrname, password, hashed_password, salt, email, phone)
            print(f"Welome to SuperBroker {usrname}!")
            cls.save_user(user)
            return user
        except ValueError as err:
            print(err)
            return cls.sign_up()  # tal vez esto se podría dejar fuera de la función.

    @classmethod
    def save_user(cls, usr):
        with open(cls.file_path, "a", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["usrname", "password", "salt", "email", "phone"]
            )
            writer.writerow(
                {
                    "usrname": usr.usrname,
                    "password": usr.hashed_password,
                    "salt": usr.salt,
                    "email": usr.email,
                    "phone": usr.phone,
                }
            )

    @classmethod
    def login(cls):
        print("Login")
        usrname = input("Username: ")
        password = input("Password: ")
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            if cls.check_usr(usrname) == True:
                for row in reader:
                    if cls.check_password(password, row["hashed_password"], row["salt"]):
                        print(f"Welcome {usrname}!")
                        return True
                else:
                    print("Wrong password")
                    return False
            else:
                print("User does not exist")
                return False

    def __init__(self, usrname, password, hashed_password, salt, email, phone):
        self.usrname = usrname
        self.password = password
        self.hashed_password = User.hash_password(password, salt)[0]
        self.salt = User.hash_password(password, salt)[1]
        self.email = email
        self.phone = phone

    def __str__(self):
        return (
            "Username: "
            + self.usrname
            + " Password: "
            + self.hashed_password        
            + " Email: "
            + self.email
            + " Phone: "
            + self.phone
        )

    # Getter => @property
    @property 
    def usrname(self):
        return self._usrname
    # _ use for the function not to colide with the variable
    # _name is a private variable (honor system, not forced)

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
        elif User.check_usr(usrname) == True:
            raise ValueError("User already exists")
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

def main():
    #User.sign_up()
    User.login()


main()
