import pytest

from finances.savings_account_year import SavingsAccountYear


class TestProjections:
    @pytest.fixture
    def account(self) -> SavingsAccountYear:
        return SavingsAccountYear(10000, interest_rate=10, capital_gains=7000)

    def test_starting_balance(self, account):
        assert 10000, account.starting_balance

    def test_ending_balance_applies_interest_rate(self, account):
        assert account.ending_balance == 11000

    def test_next_years_starting_balance_equals_this_years_ending_balance(self, account):
        next_year = account.next_year()
        assert next_year.starting_balance == account.ending_balance

    def test_next_years_interest_rate_equals_this_years_interest_rate(self, account):
        next_year = account.next_year()
        assert next_year.interest_rate == account.interest_rate

    def test_interest_rate_matches_constructor(self, account):
        assert account.interest_rate == 10

    def test_withdraw_funds_happens_at_the_beginning_of_a_year(self, account):
        account.withdraw(1000)
        assert account.ending_balance == 9900

    def test_starting_principal(self, account):
        assert account.starting_principal == 3000

    def test_ending_principal(self, account):
        assert account.starting_principal == 3000
        account.withdraw(2000)
        assert account.ending_principal == 1000

    def test_ending_principal_never_goes_below_0(self, account):
        account.withdraw(4000)
        assert account.ending_principal == 0

    @pytest.mark.skip
    def test_withdrawing_more_than_principal_incurs_capital_gains_tax(self):
        account = SavingsAccountYear(10000, interest_rate=10, capital_gains=7000)
        account.withdraw(3000)
        assert account.ending_balance == 7700
        account.withdraw(5000)
        assert account.ending_balance == 2000 + 200 - (5000 * 0.25)

    @pytest.mark.skip(reason='Todo')
    def test_multiple_withdrawals_in_a_year(self): ...
