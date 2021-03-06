import pytest

from finances.domain.dollars import Dollars
from finances.domain.year import Year
from finances.ui.stock_market_table import StockMarketTableModel
from finances.domain.interest_rate import InterestRate
from finances.domain.stock_market_account import StockMarketAccount
from finances.domain.tax_rate import TaxRate

INTEREST_RATE = InterestRate(10)
CAPITAL_GAINS_TAX_RATE = TaxRate(25)
STARTING_PRINCIPAL = Dollars(7000)
STARTING_BALANCE = Dollars(10000)
STARTING_YEAR = Year(2010)
ENDING_YEAR = Year(2050)
APPRECIATION = Dollars(1000)


class TestStockMarketTable:
    @pytest.fixture
    def account(self):
        return StockMarketAccount(
            starting_year=STARTING_YEAR,
            ending_year=ENDING_YEAR,
            starting_principal=STARTING_PRINCIPAL,
            starting_balance=STARTING_BALANCE,
            interest_rate=INTEREST_RATE,
            capital_gains_tax_rate=CAPITAL_GAINS_TAX_RATE
        )

    @pytest.fixture
    def table(self, account):
        return StockMarketTableModel(account)

    def test_columns(self, table):
        assert len(table.ColumnHeadings) == 6
        assert table.ColumnHeadings[0] == ' Year '
        assert table.ColumnHeadings[1] == ' Starting Balance '
        assert table.ColumnHeadings[2] == ' Starting Principal '

    def test_one_row(self, table):
        assert table.value_at(0, 0) == STARTING_YEAR, 'year'
        assert table.value_at(0, 1) == STARTING_BALANCE, 'starting balance'
        assert table.value_at(0, 2) == STARTING_PRINCIPAL, 'starting principal'
        assert table.value_at(0, 3) == Dollars(0), 'withdrawals'
        assert table.value_at(0, 4) == Dollars(1000), 'appreciation'
        assert table.value_at(0, 5) == Dollars(11000), 'ending balance'

    def test_multiple_rows(self, table):
        assert STARTING_YEAR == table.value_at(0, 0)
        assert STARTING_BALANCE == table.value_at(0, 1)
        assert table.row_count == STARTING_YEAR.number_of_years_inclusive(ENDING_YEAR)
        assert ENDING_YEAR == table.value_at(40, 0)
        assert Dollars(11000) == table.value_at(1, 1)
