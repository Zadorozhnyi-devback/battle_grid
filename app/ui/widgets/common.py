from tkinter import Label, Tk, Frame
from typing import List


def get_selected_tab_title(cls) -> str:
    selected_tab = cls._tab_control.select()
    category = cls._tab_control.tab(selected_tab, 'text')
    return category


def create_empty_strings(window: [Tk, Frame], rows: List[int]) -> None:
    for row in rows:
        empty_string = Label(master=window, text='')
        empty_string.grid(column=0, row=row)


def create_empty_column(window: [Tk, Frame], columns: List[int]) -> None:
    for column in columns:
        empty_column = Label(master=window, text='')
        empty_column.grid(column=column, row=0)
