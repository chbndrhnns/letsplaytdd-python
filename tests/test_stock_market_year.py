from functools import partial
from typing import Callable

import pytest

from finances.dollar import Dollar
from finances.interest_rate import InterestRate
from finances.stock_market_year import StockMarketYear
from finances.tax_rate import TaxRate

STARTING_PRINCIPAL = Dollar(3000)
STARTING_BALANCE = Dollar(10000)
INTEREST_RATE = InterestRate(10)
CAPITAL_GAINS_TAX_RATE = TaxRate(25)


def account_factory(
        *,
        start: Dollar = None,
        interest_rate: InterestRate = None,
        starting_principal: Dollar = None,
        tax_rate: TaxRate = None):
    start = start or STARTING_BALANCE
    interest_rate = interest_rate or INTEREST_RATE
    tax_rate = tax_rate or CAPITAL_GAINS_TAX_RATE
    starting_principal = starting_principal or STARTING_PRINCIPAL
    return StockMarketYear(
        start,
        interest_rate=interest_rate,
        starting_principal=starting_principal,
        capital_gains_tax_rate=tax_rate
    )


@pytest.fixture
def default_account() -> Callable[[], StockMarketYear]:
    return partial(account_factory, interest_rate=INTEREST_RATE)


class TestStockMarketYear:

    @pytest.fixture
    def year(self, default_account) -> StockMarketYear:
        return default_account()

    def test_starting_values(self, year):
        assert 10000, year.starting_balance
        assert year.interest_rate == INTEREST_RATE
        assert year.starting_principal == Dollar(3000)
        assert year.capital_gains_tax_rate == CAPITAL_GAINS_TAX_RATE

    def test_ending_balance(self, year):
        assert year.ending_balance == Dollar(11000), 'ending balance includes interest'
        year.withdraw(1000)
        assert year.ending_balance == Dollar(9900), 'ending balance includes withdrawals'
        year.withdraw(3000)
        assert year.ending_balance == Dollar(6233), 'ending balance includes capital gains tax withdrawals'

    def test_next_years_values(self, year):
        next_year = year.next_year()
        assert next_year.starting_balance == year.ending_balance
        assert next_year.interest_rate == year.interest_rate
        assert next_year.starting_principal == year.ending_principal
        assert next_year.capital_gains_tax_rate == year.capital_gains_tax_rate

    def test_ending_principal(self, year):
        year.withdraw(1000)
        assert year.ending_principal == Dollar(9000), 'considers withdrawals'
        year.withdraw(2000)
        assert year.ending_principal == Dollar(7000), 'considers totals of multiple withdrawals'
        year.withdraw(8000)
        assert year.ending_principal == Dollar(0), 'never goes below zero'

    def test_total_withdrawn_including_capital_gains(self, year):
        year = account_factory(
            start=STARTING_BALANCE, interest_rate=INTEREST_RATE, starting_principal=Dollar(0)
        )
        year.withdraw(1000)
        assert year.capital_gains_tax_incurred == Dollar(333)
        assert year.total_withdrawn == Dollar(1333)

    def test_capital_gains_tax(self, year):
        year.withdraw(4000)
        capital_gains_tax = Dollar(year.capital_gains_tax_rate.simple_tax_for(1000))
        additional_withdrawals_to_cover_tax = Dollar(83)
        assert year.capital_gains_tax_incurred == additional_withdrawals_to_cover_tax + capital_gains_tax
        assert year.total_withdrawn == Dollar(4000) + capital_gains_tax + additional_withdrawals_to_cover_tax

    def test_interest_earned(self, year):
        assert year.interest_earned == Dollar(1000), 'basic interest earned'
        year.withdraw(2000)
        assert year.interest_earned == Dollar(800), 'withdrawals do not earn interest'
        year.withdraw(2000)
        assert year.interest_earned == Dollar(566), 'capital gains taxes do not earn interest'
