from tkinter import Tk, Canvas, Label

from settings.ui.const import (
    MY_FONT, CURR_PATH_LABEL_COORDS, CURR_PATH, DEFAULT_FONT_SIZE
)


def get_curr_path_label(main_window: Tk, destination_path: str) -> Label:
    curr_path_label = Label(
        master=main_window,
        font=(MY_FONT, DEFAULT_FONT_SIZE),
        text=f'{CURR_PATH}: {destination_path}'
    )
    curr_path_label.grid(
        **CURR_PATH_LABEL_COORDS, sticky='W', columnspan=100
    )
    return curr_path_label


# def change_text_canvas(main_canvas, text: str, main_text_id) -> None:
#     # first set coords to default
#     main_canvas.coords(main_text_id, 5, 5)
#     main_canvas.itemconfig(
#         tagOrId=main_text_id, text=text
#     )


def get_canvas(
    main_window: Tk, column: int, row: int,
    padding_top: int, text: str, font_size: int
) -> Canvas:
    canvas = Canvas(master=main_window)
    canvas.grid(column=column, row=row, sticky='W')
    txt = canvas.create_text(
        5, padding_top, text=text,
        font=(MY_FONT, font_size), anchor='nw'
    )
    bbox = canvas.bbox(txt)
    # size without padding on y bottom and long width
    canvas.configure(height=bbox[3], width=bbox[2])
    return canvas
