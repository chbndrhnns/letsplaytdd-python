import pytest

from finances.dollars import Dollars
from finances.gui import StockMarketTable
from finances.interest_rate import InterestRate
from finances.tax_rate import TaxRate

INTEREST_RATE = InterestRate(10)
CAPITAL_GAINS_TAX_RATE = TaxRate(25)
STARTING_PRINCIPAL = Dollars(7000)
STARTING_BALANCE = Dollars(10000)
YEAR = 2010
APPRECIATION = Dollars(1000)


class TestStockMarketTable:

    @pytest.fixture
    def table(self):
        return StockMarketTable(
            year=YEAR,
            starting_balance=STARTING_BALANCE,
            starting_principal=STARTING_PRINCIPAL,
            interest_rate=INTEREST_RATE,
            capital_gains_tax_rate=CAPITAL_GAINS_TAX_RATE,
        )

    def test_columns(self, table):
        assert len(table.ColumnHeadings) == 6
        assert table.ColumnHeadings[0] == 'Year'
        assert table.ColumnHeadings[1] == 'Starting Balance'
        assert table.ColumnHeadings[2] == 'Starting Principal'

    def test_first_row(self, table):
        assert table.value_at(0, 0) == YEAR
        assert table.value_at(0, 1) == STARTING_BALANCE
        assert table.value_at(0, 2) == STARTING_PRINCIPAL
        assert table.value_at(0, 3) == Dollars(0)
        assert table.value_at(0, 4) == Dollars(1000)
        assert table.value_at(0, 5) == Dollars(11000)
