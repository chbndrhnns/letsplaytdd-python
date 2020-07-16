from finances.savings_account import SavingsAccount


def test_deposit():
    account = SavingsAccount()
    account.deposit(100)
    assert account.balance == 100


def test_withdraw():
    account = SavingsAccount()
    account.deposit(100)
    account.withdraw(50)
    assert account.balance == 50


def test_negative_balance_is_fine():
    account = SavingsAccount()
    account.withdraw(75)
    assert account.balance == -75
