import pytest

from finances.dollars import Dollars
from finances.gui import StockMarketTable
from finances.interest_rate import InterestRate
from finances.tax_rate import TaxRate

INTEREST_RATE = InterestRate(10)
CAPITAL_GAINS_TAX_RATE = TaxRate(25)
STARTING_PRINCIPAL = Dollars(7000)
STARTING_BALANCE = Dollars(10000)
STARTING_YEAR = 2010
ENDING_YEAR = 2050
APPRECIATION = Dollars(1000)


class TestStockMarketTable:

    @pytest.fixture
    def table(self):
        return StockMarketTable(
            starting_year=STARTING_YEAR, starting_balance=STARTING_BALANCE,
            starting_principal=STARTING_PRINCIPAL, interest_rate=INTEREST_RATE,
            capital_gains_tax_rate=CAPITAL_GAINS_TAX_RATE, ending_year=ENDING_YEAR)

    def test_columns(self, table):
        assert len(table.ColumnHeadings) == 6
        assert table.ColumnHeadings[0] == 'Year'
        assert table.ColumnHeadings[1] == 'Starting Balance'
        assert table.ColumnHeadings[2] == 'Starting Principal'

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
        assert table.row_count == ENDING_YEAR - STARTING_YEAR + 1
        assert ENDING_YEAR == table.value_at(40, 0)
        assert Dollars(11000) == table.value_at(1, 1)
