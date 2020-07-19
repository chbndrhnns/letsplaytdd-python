import pytest

from finances.savings_account_year import SavingsAccountYear


@pytest.fixture
def interest_rate():
    return 10


@pytest.fixture
def create_account(interest_rate) -> SavingsAccountYear:
    def factory(*, start: int = 10000, interest_rate=interest_rate, starting_principal=3000):
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

    def test_withdrawn_funds_do_not_earn_interest(self, year):
        year.withdraw(1000)
        assert year.ending_balance == 9900

    def test_multiple_withdrawals_in_a_year_are_totalled(self, year):
        year.withdraw(1000)
        year.withdraw(3000)
        assert year.total_withdrawals == 4000

    def test_starting_principal(self, year):
        assert year.starting_principal == 3000

    def test_ending_principal_considers_withdrawals(self, year):
        year.withdraw(2000)
        assert year.ending_principal == 1000

    def test_ending_principal_never_goes_below_0(self, year):
        year.withdraw(4000)
        assert year.ending_principal == 0

    def test_withdrawing_more_than_principal_takes_from_capital_gains(self, year):
        year.withdraw(1000)
        assert year.capital_gains_withdrawn == 0
        year.withdraw(3000)
        assert year.capital_gains_withdrawn == 1000

    def test_capital_gains_tax_incurred__needs_to_cover_capital_gains_withdrawn_AND_additional_capital_gains_withdrawn_to_pay_tax(
            self, year):
        year.withdraw(5000)
        assert year.capital_gains_withdrawn == 2000
        assert year.capital_gains_tax_incurred() == 666

    def test_ending_capital_gains_includes_interest_earned(self, year):
        assert year.starting_capital_gains == 7000
        assert year.ending_capital_gains == 4000

    def test_capital_gains_tax_is_included_in_ending_balance(self, year, interest_rate):
        ending_balance_multiplier = (1 + interest_rate) / interest_rate

        expected_capital_gains_tax = 666
        amount_withdrawn = 5000
        expected_starting_balance_after_withdrawals = 10000 - amount_withdrawn - expected_capital_gains_tax
        year.withdraw(amount_withdrawn)
        assert year.capital_gains_withdrawn == 2000
        assert year.ending_balance == int(expected_starting_balance_after_withdrawals * ending_balance_multiplier)
