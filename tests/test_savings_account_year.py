from finances.savings_account_year import SavingsAccountYear


class TestBasics:
    def test_deposit(self):
        account = SavingsAccountYear()
        account.deposit(100)
        assert account.balance == 100

    def test_withdraw(self):
        account = SavingsAccountYear()
        account.deposit(100)
        account.withdraw(50)
        assert account.balance == 50

    def test_negative_balance_is_fine(self):
        account = SavingsAccountYear()
        account.withdraw(75)
        assert account.balance == -75


class TestProjections:
    def test_next_year(self):
        account = SavingsAccountYear(10000)
        next_year_account = account.next_year(10)
        assert next_year_account.balance == 11000
