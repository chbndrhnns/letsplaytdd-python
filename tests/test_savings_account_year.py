import pytest

from finances.savings_account_year import SavingsAccountYear


class TestProjections:
    @pytest.fixture
    def account(self):
        return SavingsAccountYear(10000, interest_rate=10)

    def test_starting_balance(self, account):
        assert 10000, account.starting_balance

    def test_ending_balance(self, account):
        assert account.ending_balance == 11000

    def test_next_years_starting_balance_equals_this_years_ending_balance(self, account):
        next_year = account.next_year()
        assert next_year.starting_balance == account.ending_balance

    def test_next_years_interest_rate_equals_this_years_interest_rate(self, account):
        next_year = account.next_year()
        assert next_year.interest_rate == account.interest_rate

    def test_interest_rate(self, account):
        assert account.interest_rate == 10
