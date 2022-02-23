from tkinter import Label, Tk, Frame
from typing import List


def create_empty_strings(window: [Tk, Frame], rows: List[int]) -> None:
    for row in rows:
        empty_string = Label(master=window, text='')
        empty_string.grid(column=0, row=row)
