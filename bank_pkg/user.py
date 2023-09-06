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
            + " Password: "
            + "********"  # self.password
            + " Email: "
            + self.email
            + " Phone: "
            + self.phone
        )

    @classmethod
    def sign_up(cls):
        print("Sign up")
        name = input("Name: ")
        password = input("Password: ")
        email = input("Email: ")
        phone = input("Phone: ")
        try:
            user = cls(name, password, email, phone)
            return user
        except ValueError as err:
            print(err)
            return User.sign_up()  # tal vez esto hay que dejarlo fuera de la función.

    # Getter => @property
    # _ use for the function not to colide with the variable
    # _name is a private variable (honor system, not forced)
    @property
    def name(self):
        return self._name

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
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

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
        user = input("user: ")
        password = input("password: ")
        print(f"Hello User: {user}")


def main():
    users = []
    print("Main ()")
    users.append(User.sign_up())
    users.append(User.sign_up())
    for user in users:
        print(user)


main()
