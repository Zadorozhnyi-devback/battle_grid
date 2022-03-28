from tkinter import Entry, Tk, Frame, Toplevel
from typing import Union


def get_input(
    window: Union[Frame, Tk, Toplevel], row: int, column: int
) -> Entry:
    my_input = Entry(master=window, width=17)
    my_input.grid(column=column, row=row, sticky='W')
    my_input.focus()
    return my_input
