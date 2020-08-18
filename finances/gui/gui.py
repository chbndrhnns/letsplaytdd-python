from typing import Optional, List

import PySimpleGUI as sg

from finances.dollars import Dollars
from finances.interest_rate import InterestRate
from finances.stock_market_year import StockMarketYear
from finances.tax_rate import TaxRate

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

    def __init__(self, *, starting_year: int, starting_balance: Dollars, starting_principal: Dollars,
                 interest_rate: InterestRate,
                 capital_gains_tax_rate: TaxRate, ending_year: int):

        self._starting_year = starting_year
        self._ending_year = ending_year

        self._years: List[StockMarketYear] = [None] * self.row_count
        values = self._populate_years(starting_balance=starting_balance, starting_principal=starting_principal,
                                      interest_rate=interest_rate,
                                      capital_gains_tax_rate=capital_gains_tax_rate)

        super().__init__(
            values=values,
            key='years',
            headings=self.headings,
            auto_size_columns=True,
            num_rows=20
        )

    @property
    def row_count(self):
        return self._ending_year - self._starting_year + 1

    def _populate_years(self, *, starting_balance, starting_principal, interest_rate,
                        capital_gains_tax_rate):

        values = []
        self._years[0] = StockMarketYear(
            starting_balance=starting_balance,
            starting_principal=starting_principal,
            interest_rate=interest_rate,
            capital_gains_tax_rate=capital_gains_tax_rate
        )
        for i in range(1, self.row_count):
            year: StockMarketYear = self._years[i - 1].next_year()
            self._years[i] = year
            values.append([
                self._starting_year + i,
                year.starting_balance,
                year.starting_principal,
                year.total_withdrawals,
                year.appreciation,
                year.ending_balance,
                7
            ])

        return values

    def value_at(self, row_idx, col_idx):
        year = self._years[row_idx]

        if col_idx == 0:
            return self._starting_year + row_idx
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
        return ""


def gui():
    layout = [
        [sg.Text('Personal finances')],
        [table()],
        [sg.OK(), sg.Cancel()]
    ]

    window = sg.Window(
        title="Personal finances",
        layout=layout,
        margins=(5, 5),
        size=(900, 600),
        font=('San Francisco', 15)
    )
    while True:
        event, values = window.read()
        print(event)
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break


def table():
    return StockMarketTable(
        starting_year=2010, starting_balance=Dollars(10000), starting_principal=Dollars(7000),
        interest_rate=InterestRate(10), capital_gains_tax_rate=TaxRate(25), ending_year=2050
    )


if __name__ == '__main__':
    gui()
