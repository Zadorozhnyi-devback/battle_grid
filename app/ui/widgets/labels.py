from tkinter import Tk, Canvas, Label, Frame, Toplevel
from typing import Union

from settings.ui.const import (
    MY_FONT, CURR_PATH_LABEL_COORDS, CURRENT_PATH, DEFAULT_FONT_SIZE
)


def get_curr_path_label(main_window: Tk, destination_path: str) -> Label:
    curr_path_label = Label(
        master=main_window,
        font=(MY_FONT, DEFAULT_FONT_SIZE),
        text=f'{CURRENT_PATH}: {destination_path}'
    )
    curr_path_label.grid(
        **CURR_PATH_LABEL_COORDS, sticky='W', columnspan=100
    )
    return curr_path_label


def change_text_canvas(canvas, text: str) -> None:
    # first set coords to default
    canvas.coords('1', 5, 5)
    canvas.itemconfig(tagOrId='1', text=text)


def get_canvas(
    window: Union[Frame, Tk, Toplevel], column: int, row: int, font_size: int,
    column_span: int, padding_top: int, text: str, bonus_width: int = 0,
    sticky: str = 'W'
) -> Canvas:
    canvas = Canvas(master=window)
    canvas.grid(column=column, row=row, sticky=sticky, columnspan=column_span)
    text = canvas.create_text(
        5, padding_top, text=text,
        font=(MY_FONT, font_size), anchor='nw'
    )
    bbox = canvas.bbox(text)
    # size without padding on y bottom and long width
    canvas.configure(height=bbox[3], width=bbox[2] + bonus_width)
    return canvas
