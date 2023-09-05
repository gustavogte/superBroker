class User:
    def __init__(self, name, password, email, phone):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone

    def __str__(self):
        return ("Name: " + self.name
            + " Password: " + self.password
            + " Email: " + self.email
            + " Phone: " + self.phone
        )
    
    def __add__(self):
        pass

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

def main():
    print('hello gus')
    user1 = User.sign_up()
    user2 = User.sign_up()
    users =[user1, user2]
    print(user1)
    print(type(user1))
    print(user2)
    print(type(user2))
    print(users)
    print(type(users))  

main()