from tkinter import Frame, Tk, Toplevel, Canvas, Label
from typing import Union

from app.settings.ui.const import (
    ARIAL_BOLD,
    CURR_PATH_LABEL_COORDS,
    CURRENT_PATH,
    DEFAULT_FONT_SIZE
)


def get_curr_path_label(main_window: Tk, destination_path: str) -> Label:
    curr_path_label = Label(
        master=main_window,
        font=(ARIAL_BOLD, DEFAULT_FONT_SIZE),
        text=f'{CURRENT_PATH}: {destination_path}'
    )
    curr_path_label.grid(**CURR_PATH_LABEL_COORDS)
    return curr_path_label


def get_canvas(
    frame: Union[Frame, Tk, Toplevel],
    column: int,
    row: int,
    font_size: int,
    column_span: int,
    padding_top: int,
    text: str,
    sticky: str,
    bonus_width: int = 0
) -> Canvas:
    canvas = Canvas(master=frame)
    canvas.grid(column=column, row=row, sticky=sticky, columnspan=column_span)
    text = canvas.create_text(
        5,
        padding_top,
        text=text,
        font=(ARIAL_BOLD, font_size),
        anchor='nw'
    )
    bbox = canvas.bbox(text)
    # size without padding on y bottom and long width
    canvas.configure(height=bbox[3], width=bbox[2] + bonus_width)
    return canvas
