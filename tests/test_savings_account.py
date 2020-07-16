class SavingsAccount(object):

    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        self._balance -= amount


def test_deposit():
    account = SavingsAccount()
    account.deposit(100)
    assert account.balance == 100


def test_withdraw():
    account = SavingsAccount()
    account.deposit(100)
    account.withdraw(50)
    assert account.balance == 50
