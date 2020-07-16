class SavingsAccountYear(object):

    def __init__(self, starting_balance: int = 0, *, interest_rate: int = 0):
        self._balance = starting_balance
        self._interest_rate = interest_rate

    @property
    def starting_balance(self):
        return self._balance

    @property
    def ending_balance(self):
        return int(self.starting_balance * ((100 + self.interest_rate) / 100))

    @property
    def interest_rate(self):
        return self._interest_rate

    def next_year(self):
        result = SavingsAccountYear(self.ending_balance, interest_rate=self.interest_rate)
        return result
