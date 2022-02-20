from tkinter import Entry, Tk


def get_input(main_window: Tk, row: int, column: int) -> Entry:
    my_input = Entry(master=main_window, width=20)
    my_input.grid(column=column, row=row, sticky='W')
    my_input.focus()
    return my_input
