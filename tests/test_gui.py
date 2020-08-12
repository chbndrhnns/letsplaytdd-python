import pytest

from finances.gui import StockMarketTable


class TestStockMarketTable:
    @pytest.fixture
    def table(self):
        return StockMarketTable()

    def test_columns(self, table):
        assert len(table.ColumnHeadings) == 7
        assert table.ColumnHeadings[0] == 'Year'
        assert table.ColumnHeadings[1] == 'Starting Balance'
        assert table.ColumnHeadings[2] == 'Starting Principal'

    def test_first_row(self, table):
        ...
