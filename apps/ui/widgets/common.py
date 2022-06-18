from tkinter import Label, Tk, Frame
from typing import List


__all__ = (
    'create_empty_strings',
    'create_empty_columns'
)


def create_empty_strings(frame: [Tk, Frame], rows: List[int]) -> None:
    for row in rows:
        empty_string = Label(master=frame, text='')
        empty_string.grid(column=0, row=row)


def create_empty_columns(frame: [Tk, Frame], columns: List[int]) -> None:
    for column in columns:
        empty_column = Label(master=frame, text='')
        empty_column.grid(column=column, row=0)
