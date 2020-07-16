class SavingsAccount(object):

    def __init__(self, initial_balance: int = 0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        self._balance -= amount
