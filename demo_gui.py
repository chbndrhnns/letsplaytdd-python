import PySimpleGUI as sg


def gui():
    layout = [
        [sg.Text('Personal finances')],
        [sg.Table(
            headings=['One', 'Two'],
            values=[[x, 2, 3] for x in range(80)],
            auto_size_columns=True
        )],
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


if __name__ == '__main__':
    gui()
