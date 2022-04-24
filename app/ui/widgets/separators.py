from tkinter import Frame
from tkinter.ttk import Separator
from typing import Tuple


def create_separator(
    frame: Frame,
    orient: str,
    row_span: int,
    sticky: str,
    column: int, row: int,
    pad_y: Tuple[int], pad_x: Tuple[int]
) -> None:
    separator = Separator(master=frame, orient=orient)
    separator.grid(
        column=column, row=row,
        pady=pad_y, padx=pad_x,
        rowspan=row_span,
        sticky=sticky,
    )
