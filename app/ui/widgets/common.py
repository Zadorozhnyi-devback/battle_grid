from tkinter import Label, Tk
from typing import List


def create_empty_strings(main_window: Tk, rows: List[int]) -> None:
    for row in rows:
        empty_string = Label(master=main_window, text='')
        empty_string.grid(column=0, row=row)
