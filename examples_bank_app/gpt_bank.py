import csv
import os
import hashlib
import secrets  # to generate a secure random salt


class Bank:
    file_path = "bank_data.csv"

    @classmethod
    def initialize_csv(cls):
        if not os.path.exists(cls.file_path):
            with open(cls.file_path, "w", newline="") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["username", "password", "salt", "balance"]
                )
                writer.writeheader()

    @classmethod
    def hash_password(cls, password, salt=None):
        if not salt:
            salt = secrets.token_hex(16)
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return password_hash, salt

    @classmethod
    def sign_up(cls, username, password):
        hashed_password, salt = cls.hash_password(password)
        with open(cls.file_path, "a", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["username", "password", "salt", "balance"]
            )
            writer.writerow(
                {
                    "username": username,
                    "password": hashed_password,
                    "salt": salt,
                    "balance": 0,
                }
            )  # initial balance is 0

    @classmethod
    def check_password(cls, password, hashed_password, salt):
        return hashed_password == cls.hash_password(password, salt)[0]

    @classmethod
    def login(cls, username, password):
        with open(cls.file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username and cls.check_password(
                    password, row["password"], row["salt"]
                ):
                    return True, float(row["balance"])
            return False, None


Bank.initialize_csv()
