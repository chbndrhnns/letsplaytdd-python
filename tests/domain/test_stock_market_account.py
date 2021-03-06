import pytest

from finances.domain.dollars import Dollars
from finances.domain.stock_market_account import StockMarketAccount
from finances.domain.year import Year
from tests.conftest import STARTING_BALANCE, STARTING_PRINCIPAL, INTEREST_RATE, CAPITAL_GAINS_TAX_RATE

STARTING_YEAR = Year(2010)
ENDING_YEAR = Year(2050)


@pytest.fixture
def account():
    return StockMarketAccount(
        starting_year=STARTING_YEAR, ending_year=ENDING_YEAR,
        starting_principal=STARTING_PRINCIPAL,
        starting_balance=STARTING_BALANCE,
        interest_rate=INTEREST_RATE,
        capital_gains_tax_rate=CAPITAL_GAINS_TAX_RATE
    )


class TestStockMarketAccount:

    def test_number_of_years(self, account):
        assert account.number_of_years == 41

    def test_stock_market_account_contains_multiple_years(self, account):
        assert account.get_year_offset(0).starting_balance == STARTING_BALANCE
        assert account.get_year_offset(1).starting_balance == Dollars(11000)
        assert account.get_year_offset(2).starting_balance == Dollars(12100)

    def test_no_cumulative_rounding_error_due_to_interest_calculations(self, account):
        assert account.get_year_offset(40).ending_balance == Dollars(497852)
