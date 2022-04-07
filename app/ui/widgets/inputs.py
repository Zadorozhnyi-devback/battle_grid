from tkinter import Entry, Tk, Frame, Toplevel
from typing import Union


def get_input(
    frame: Union[Frame, Tk, Toplevel], row: int, column: int, sticky: str
) -> Entry:
    my_input = Entry(master=frame, width=17)
    my_input.grid(column=column, row=row, sticky=sticky)
    my_input.focus()
    return my_input
