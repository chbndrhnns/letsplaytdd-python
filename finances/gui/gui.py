import PySimpleGUI as sg

from finances.dollars import Dollars
from finances.gui import StockMarketTable
from finances.interest_rate import InterestRate
from finances.tax_rate import TaxRate


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
