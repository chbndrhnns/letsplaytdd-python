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
        next_year = this_year.next_year()
        assert next_year.starting_balance == this_year.ending_balance

    def test_next_years_interest_rate_equals_this_years_interest_rate(self):
        this_year = SavingsAccountYear(10000)
        next_year = this_year.next_year()
        assert next_year.interest_rate == this_year.interest_rate

    def test_interest_rate(self):
        account = SavingsAccountYear(10000, interest_rate=10)
        assert account.interest_rate == 10
