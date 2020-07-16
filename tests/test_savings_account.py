from finances.savings_account import SavingsAccount


class TestBasics:
    def test_deposit(self):
        account = SavingsAccount()
        account.deposit(100)
        assert account.balance == 100

    def test_withdraw(self):
        account = SavingsAccount()
        account.deposit(100)
        account.withdraw(50)
        assert account.balance == 50

    def test_negative_balance_is_fine(self):
        account = SavingsAccount()
        account.withdraw(75)
        assert account.balance == -75


class TestProjections:
    def test_next_year(self):
        account = SavingsAccount(10000)
