from money.savings_account import SavingsAccount


def test_deposit():
    account = SavingsAccount()
    account.deposit(100)
    assert account.balance == 100


def test_withdraw():
    account = SavingsAccount()
    account.deposit(100)
    account.withdraw(50)
    assert account.balance == 50
