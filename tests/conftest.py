from functools import partial
from typing import Callable

import pytest

from finances.domain.dollars import Dollars
from finances.domain.interest_rate import InterestRate
from finances.domain.stock_market_year import StockMarketYear
from finances.domain.tax_rate import TaxRate
from finances.domain.year import Year

YEAR = Year(2010)
STARTING_PRINCIPAL = Dollars(3000)
STARTING_BALANCE = Dollars(10000)
INTEREST_RATE = InterestRate(10)
CAPITAL_GAINS_TAX_RATE = TaxRate(25)


def year_factory(
        *,
        year: YEAR = None,
        starting_balance: Dollars = None,
        interest_rate: InterestRate = None,
        starting_principal: Dollars = None,
        tax_rate: TaxRate = None):
    year = year or YEAR
    starting_balance = starting_balance or STARTING_BALANCE
    interest_rate = interest_rate or INTEREST_RATE
    tax_rate = tax_rate or CAPITAL_GAINS_TAX_RATE
    starting_principal = starting_principal or STARTING_PRINCIPAL
    return StockMarketYear(
        starting_balance=starting_balance,
        year=year,
        interest_rate=interest_rate,
        starting_principal=starting_principal,
        capital_gains_tax_rate=tax_rate
    )


@pytest.fixture
def default_year() -> Callable[[], StockMarketYear]:
    return partial(year_factory, interest_rate=INTEREST_RATE)
