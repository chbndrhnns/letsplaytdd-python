import PySimpleGUI as sg  # type: ignore

from finances.domain.dollars import Dollars
from finances.domain.year import Year
from finances.ui import StockMarketTableModel
from finances.domain.interest_rate import InterestRate
from finances.domain.stock_market_account import StockMarketAccount
from finances.domain.tax_rate import TaxRate


def run_app():
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


def account():
    return StockMarketAccount(
        starting_year=Year(2010), starting_balance=Dollars(10000), starting_principal=Dollars(7000),
        interest_rate=InterestRate(10), capital_gains_tax_rate=TaxRate(25), ending_year=Year(2050)
    )


def table():
    return StockMarketTableModel(account())


if __name__ == '__main__':
    run_app()
