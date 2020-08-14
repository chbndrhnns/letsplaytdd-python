import PySimpleGUI as sg

from finances.dollars import Dollars
from finances.stock_market_year import StockMarketYear

COLUMN_TITLES = {
    0: 'Year',
    1: 'Starting Balance',
    2: 'Starting Principal',
    3: 'Withdrawals',
    4: 'Appreciation',
    5: 'Ending Balance'

}


class StockMarketTable(sg.Table):
    headings = list(COLUMN_TITLES.values())

    def __init__(self, values=None, *, year, starting_balance, starting_principal, interest_rate,
                 capital_gains_tax_rate):
        self._year = year
        self._market_year = StockMarketYear(
            starting_balance=starting_balance,
            starting_principal=starting_principal,
            interest_rate=interest_rate,
            capital_gains_tax_rate=capital_gains_tax_rate
        )

        row = [[year, starting_balance, starting_principal, 4, 5, 6, 7]]
        values = values or []
        values.extend(row)
        values.extend([['' for _ in range(15)] for _ in enumerate(self.headings)])

        super().__init__(
            values=values,
            headings=self.headings,
            auto_size_columns=True,
            num_rows=20
        )

    def value_at(self, row_idx, col_idx):
        if col_idx == 0:
            return self._year
        if col_idx == 1:
            return self._market_year.starting_balance
        if col_idx == 2:
            return self._market_year.starting_principal
        if col_idx == 3:
            return self._market_year.total_withdrawals
        if col_idx == 4:
            return self._market_year.appreciation
        if col_idx == 5:
            return self._market_year.ending_balance
        return ""


def gui():
    layout = [
        [sg.Text('Personal finances')],
        table(),
        [sg.OK(), sg.Cancel()]
    ]

    window = sg.Window(title="Personal finances", layout=layout, margins=(100, 50))
    while True:
        event, values = window.read()
        print(event)
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break


def table():
    return [
        StockMarketTable(year=2010, starting_balance=Dollars(10000), starting_principal=Dollars(7000), interest_rate=10,
                         capital_gains_tax_rate=25)]


if __name__ == '__main__':
    gui()
