from finances.gui import StockMarketTable


class TestStockMarketTable:
    def test_columns(self):
        table = StockMarketTable()
        assert len(table.ColumnHeadings) == 7
        assert table.ColumnHeadings[0] == 'Year'
        assert table.ColumnHeadings[1] == 'Starting Balance'
        assert table.ColumnHeadings[2] == 'Starting Principal'

