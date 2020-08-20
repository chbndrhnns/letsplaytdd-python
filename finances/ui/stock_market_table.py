import PySimpleGUI as sg  # type: ignore

from finances.domain.stock_market_account import StockMarketAccount

COLUMN_TITLES_MAP = {
    0: 'Year',
    1: 'Starting Balance',
    2: 'Starting Principal',
    3: 'Withdrawals',
    4: 'Appreciation',
    5: 'Ending Balance'

}


class StockMarketTableModel(sg.Table):
    headings = [f' {col_name} ' for col_name in
                COLUMN_TITLES_MAP.values()]  # add space to tweak column width calculations

    def __init__(self, account: StockMarketAccount):

        self._account = account

        super().__init__(
            values=self.rows,
            key='years',  # noqa
            headings=self.headings,
            auto_size_columns=True,
            num_rows=20,
            font=('Menlo', 15)  # noqa
        )

    @property
    def row_count(self):
        return self._account.number_of_years

    @property
    def rows(self):
        values = []
        for row_idx in range(self._account.number_of_years):
            row = []
            for col_idx in range(len(COLUMN_TITLES_MAP)):
                row.append(self.value_at(row_idx, col_idx))
            values.append(row)
        return values

    def value_at(self, row_idx, col_idx):
        year = self._account.get_year_offset(row_idx)

        if col_idx == 0:
            return year.year
        if col_idx == 1:
            return year.starting_balance
        if col_idx == 2:
            return year.starting_principal
        if col_idx == 3:
            return year.total_withdrawals
        if col_idx == 4:
            return year.appreciation
        if col_idx == 5:
            return year.ending_balance

        assert False, 'Not implemented'
