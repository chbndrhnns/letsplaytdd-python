import PySimpleGUI as sg


class StockMarketTable(sg.Table):
    headings = [
        'Year',
        'Starting Balance',
        'Starting Principal',
        'Withdrawals',
        'Appreciation',
        'Deposits',
        'Ending Balance'
    ]

    def __init__(self, values=None):
        row = [[1, 2, 3, 4, 5, 6, 7]]
        values = values or []
        values.extend(row)
        values.extend([['' for _ in range(15)] for _ in enumerate(self.headings)])

        super().__init__(
            values=values,
            headings=self.headings,
            auto_size_columns=True,
            num_rows=20
        )


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
    return [StockMarketTable()]


if __name__ == '__main__':
    gui()
