import pytest

from finances.savings_account_year import SavingsAccountYear


@pytest.fixture
def create_account() -> SavingsAccountYear:
    def factory(*, start: int = 10000, interest_rate=10, starting_principal=3000):
        return SavingsAccountYear(
            start,
            interest_rate=interest_rate,
            starting_principal=starting_principal
        )

    return factory


class TestProjections:

    @pytest.fixture
    def year(self, create_account) -> SavingsAccountYear:
        return create_account()

    def test_starting_balance(self, year):
        assert 10000, year.starting_balance

    def test_ending_balance_applies_interest_rate(self, year):
        assert year.ending_balance == 11000

    def test_next_years_starting_balance_equals_this_years_ending_balance(self, year):
        next_year = year.next_year()
        assert next_year.starting_balance == year.ending_balance

    def test_next_years_interest_rate_equals_this_years_interest_rate(self, year):
        next_year = year.next_year()
        assert next_year.interest_rate == year.interest_rate

    def test_interest_rate_matches_constructor(self, year):
        assert year.interest_rate == 10

    def test_withdraw_funds_happens_at_the_beginning_of_a_year(self, year):
        year.withdraw(1000)
        assert year.ending_balance == 9900

    def test_multiple_withdrawals_in_a_year(self, year):
        year.withdraw(1000)
        year.withdraw(3000)
        assert year.total_withdrawals == 4000

    def test_starting_principal(self, year):
        assert year.starting_principal == 3000

    def test_ending_principal(self, year):
        assert year.starting_principal == 3000
        year.withdraw(2000)
        assert year.ending_principal == 1000

    def test_ending_principal_never_goes_below_0(self, year):
        year.withdraw(4000)
        assert year.ending_principal == 0

    def test_capital_gains_withdrawn(self, year):
        assert year.starting_principal == 3000
        year.withdraw(1000)
        assert year.capital_gains_withdrawn == 0
        year.withdraw(3000)
        assert year.capital_gains_withdrawn == 1000

    # @pytest.mark.skip
    # def test_withdrawing_more_than_principal_incurs_capital_gains_tax(self, year):
    #     year.withdraw(3000)
    #     assert year.ending_balance == 7700
    #     year.withdraw(5000)
    #     assert year.ending_balance == 2000 + 200 - (5000 * 0.25)
