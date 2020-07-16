class SavingsAccountYear(object):

    def __init__(self, starting_balance: int = 0, *, interest_rate: int = 0):
        self._balance = starting_balance
        self._interest_rate = interest_rate

    @property
    def starting_balance(self):
        return self._balance

    @property
    def ending_balance(self):
        return int(self._balance * ((100 + self._interest_rate) / 100))

    def withdraw(self, amount: int):
        self._balance -= amount

    def deposit(self, amount: int):
        self._balance += amount

    def next_year(self):
        result = SavingsAccountYear(self.ending_balance, interest_rate=0)
        return result
