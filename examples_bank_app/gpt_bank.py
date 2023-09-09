import csv
import os
import bcrypt

class Bank:
    
    file_path = "bank_data.csv"
    
    @classmethod
    def initialize_csv(cls):
        if not os.path.exists(cls.file_path):
            with open(cls.file_path, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["username", "password", "balance"])
                writer.writeheader()
    
    @classmethod
    def hash_password(cls, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    @classmethod
    def sign_up(cls, username, password):
        hashed_password = cls.hash_password(password)
        with open(cls.file_path, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["username", "password", "balance"])
            writer.writerow({"username": username, "password": hashed_password, "balance": 0})  # initial balance is 0
    
    @classmethod
    def check_password(cls, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    @classmethod
    def login(cls, username, password):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username and cls.check_password(password, row["password"]):
                    return True, float(row["balance"])
            return False, None

Bank.initialize_csv()
