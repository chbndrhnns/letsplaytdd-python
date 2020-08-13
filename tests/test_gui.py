import pytest

from finances.dollars import Dollars
from finances.gui import StockMarketTable

STARTING_PRINCIPAL = Dollars(7000)
STARTING_BALANCE = Dollars(10000)
YEAR = 2010


class TestStockMarketTable:

    @pytest.fixture
    def table(self):
        return StockMarketTable(
            year=YEAR,
            starting_balance=STARTING_BALANCE,
            starting_principal=STARTING_PRINCIPAL,
        )

    def test_columns(self, table):
        assert len(table.ColumnHeadings) == 7
        assert table.ColumnHeadings[0] == 'Year'
        assert table.ColumnHeadings[1] == 'Starting Balance'
        assert table.ColumnHeadings[2] == 'Starting Principal'

    def test_first_row(self, table):
        assert table.value_at(0, 0) == YEAR
        assert table.value_at(0, 1) == STARTING_BALANCE
        assert table.value_at(0, 2) == STARTING_PRINCIPAL
