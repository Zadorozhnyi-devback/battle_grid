from tkinter import Frame, Tk, Toplevel, Canvas
from typing import Union

from app.settings.ui.const import ARIAL_BOLD


def create_canvas(
    frame: Union[Frame, Tk, Toplevel], column: int, row: int, font_size: int,
    column_span: int, padding_top: int, text: str, sticky: str,
    bonus_width: int = 0
) -> None:
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
