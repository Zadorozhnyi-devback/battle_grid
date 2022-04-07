from tkinter import Label, Tk, Frame
from typing import List


def get_selected_tab_title(self) -> str:
    selected_tab = self._tab_control.select()
    print('selected_tab', selected_tab)
    if selected_tab:
        # print(type(selected_tab))
        category = self._tab_control.tab(selected_tab, 'text')
        return category


def create_empty_strings(frame: [Tk, Frame], rows: List[int]) -> None:
    for row in rows:
        empty_string = Label(master=frame, text='')
        empty_string.grid(column=0, row=row)


def create_empty_columns(frame: [Tk, Frame], columns: List[int]) -> None:
    for column in columns:
        empty_column = Label(master=frame, text='')
        empty_column.grid(column=column, row=0)
