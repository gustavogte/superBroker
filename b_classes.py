class Account:
    def __init__(self):
        self._balance = 0
        # "_" used because it is private so don't interfere with instances or properties.

    # this is a getter
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n
