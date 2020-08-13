import PySimpleGUI as sg

from finances.dollars import Dollars

COLUMN_TITLES = {
    0: 'Year',
    1: 'Starting Balance',
    2: 'Starting Principal',
    3: 'Withdrawals',
    4: 'Appreciation',
    5: 'Deposits',
    6: 'Ending Balance'

}


class StockMarketTable(sg.Table):
    headings = list(COLUMN_TITLES.values())

    def __init__(self, values=None, *, year, starting_balance, starting_principal):
        self._year = year
        self._starting_balance = starting_balance
        self._starting_principle = starting_principal

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
            return self._starting_balance
        if col_idx == 2:
            return self._starting_principle
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
    return [StockMarketTable(
        year=2010,
        starting_balance=Dollars(10000),
        starting_principal=Dollars(7000)
    )]


if __name__ == '__main__':
    gui()
