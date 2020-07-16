class SavingsAccount(object):

    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: int):
        self._balance += amount


def test_nothing():
    account = SavingsAccount()
    account.deposit(100)
    assert account.balance == 100
