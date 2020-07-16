from finances.savings_account_year import SavingsAccountYear


class TestProjections:
    def test_starting_balance(self):
        account = SavingsAccountYear(10000, interest_rate=10)
        assert 10000, account.starting_balance

    def test_ending_balance(self):
        account = SavingsAccountYear(10000, interest_rate=10)
        assert account.ending_balance == 11000

    def test_next_years_starting_balance_equals_this_years_ending_balance(self):
        this_year = SavingsAccountYear(10000)
        next_year_account = this_year.next_year()
        assert next_year_account.starting_balance == this_year.ending_balance
