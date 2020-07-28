from functools import partial
from typing import Callable

import pytest

from finances.stock_market_year import StockMarketYear


def account_factory(*, start: int = 10000, interest_rate=10, starting_principal=3000):
    return StockMarketYear(
        start,
        interest_rate=interest_rate,
        starting_principal=starting_principal
    )


@pytest.fixture
def interest_rate():
    return 10


@pytest.fixture
def default_account(interest_rate) -> Callable[[], StockMarketYear]:
    return partial(account_factory, interest_rate=interest_rate)


class TestStockMarketYear:

    @pytest.fixture
    def year(self, default_account) -> StockMarketYear:
        return default_account()

    def test_starting_values(self, year):
        assert 10000, year.starting_balance
        assert year.interest_rate == 10
        assert year.starting_principal == 3000

    def test_ending_balance(self, year):
        assert year.ending_balance == 11000, 'ending balance includes interest'
        year.withdraw(1000)
        assert year.ending_balance == 9900, 'ending balance includes withdrawals'
        year.withdraw(3000)
        assert year.ending_balance == 6233, 'ending balance includes capital gains tax withdrawals'

    def test_next_years_values(self, year):
        next_year = year.next_year()
        assert next_year.starting_balance == year.ending_balance
        assert next_year.interest_rate == year.interest_rate
        assert next_year.starting_principal == year.ending_principal

    def test_ending_principal(self, year):
        year.withdraw(1000)
        assert year.ending_principal == 2000, 'considers withdrawals'
        year.withdraw(2000)
        assert year.ending_principal == 0, 'considers totals of multiple withdrawals'
        year.withdraw(4000)
        assert year.ending_principal == 0, 'never goes below zero'

    def test_total_withdrawn_including_capital_gains(self, year):
        year = account_factory(
            start=10000, interest_rate=interest_rate, starting_principal=0
        )
        year.withdraw(1000)
        assert year.capital_gains_tax_incurred == 333
        assert year.total_withdrawn == 1333

    def test_capital_gains_tax(self, year, interest_rate):
        year.withdraw(4000)
        capital_gains_tax = int((1000 * year.capital_gains_tax_rate) / 100)
        additional_withdrawals_to_cover_tax = 83
        assert year.capital_gains_tax_incurred == additional_withdrawals_to_cover_tax + capital_gains_tax
        assert year.total_withdrawn == 4000 + capital_gains_tax + additional_withdrawals_to_cover_tax

    def test_interest_earned(self, year, interest_rate):
        assert year.interest_earned == 1000, 'basic interest earned'
        year.withdraw(2000)
        assert year.interest_earned == 800, 'withdrawals do not earn interest'
        year.withdraw(2000)
        assert year.interest_earned == 566, 'capital gains taxes do not earn interest'
