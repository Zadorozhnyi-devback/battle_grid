from tkinter import Frame
from tkinter.ttk import Separator
from typing import Tuple


def create_separator(
    frame: Frame, orient: str, column: int, row: int,
    row_span: int, sticky: str, pad_y: Tuple[int], pad_x: Tuple[int]
) -> None:
    separator = Separator(master=frame, orient=orient)
    separator.grid(
        column=column, row=row, rowspan=row_span,
        sticky=sticky, pady=pad_y, padx=pad_x
    )
