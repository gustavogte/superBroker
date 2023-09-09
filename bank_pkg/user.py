import csv
import os
import bcrypt
#import hashlib # is better to install bcrypt library
#import secrets  # to generate a secure random salt



class User:
    users = []
    file_path = "user_data.csv"

    @classmethod
    def initialize_csv(cls):
        if not os.path.exists(cls.file_path):
            with open(cls.file_path, "w", newline="") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["usrname", "password", "email", "phone"]
                )
                writer.writeheader()

    @classmethod
    def hash_password(cls, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    @classmethod
    def check_password(cls, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    # va a retornar True if password ok or False if not.

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
        print("Sign up")
        usrname = input("User Name: ")
        password = input("Password: ")
        hashed_password = cls.hash_password(password)
        email = input("Email: ")
        phone = input("Phone: ")
        try:
            user = cls(usrname, password, hashed_password, email, phone)
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
                file, fieldnames=["usrname", "password", "email", "phone"]
            )
            writer.writerow(
                {
                    "usrname": usr.usrname,
                    "password": usr.hashed_password,
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
            for row in reader:
                if row["usrname"] == usrname and cls.check_password(password, row["password"]):
                    print(f"Welcome {usrname}!")
                    return True
            if not cls.check_usr(usrname):
                print("User not found")
                return False
            else:
                print("Invalid password")
            return False
                
    def __init__(self, usrname, password, hashed_password, email, phone):
        self.usrname = usrname
        self.password = password
        self.hashed_password = hashed_password
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

User.initialize_csv()

def main():
    #User.sign_up()
    User.login()

main()
