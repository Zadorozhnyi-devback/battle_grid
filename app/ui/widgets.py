import os
import getpass
from pathlib import Path
from tkinter import (
    Frame, StringVar, Radiobutton, Tk, PhotoImage,
    Entry, Button, filedialog, Canvas, Label, Event,
)
from tkinter.ttk import Style
from typing import Tuple, List

from settings.ui.const import (
    WINDOW_TITLE, WINDOW_SIZE, CURR_PATH,
    DEFAULT_DOWNLOAD_PATH, MY_FONT, DESTINATION_BUTTON_TITLE,
    BUTTON_TEXT_COLOR, CREATE_BUTTON_TITLE, DESTINATION_BUTTON_SIZE,
    CREATE_BUTTON_SIZE, CREATE_BUTTON_COORDS, DESTINATION_BUTTON_COORDS,
    CURR_PATH_LABEL_COORDS, DEFAULT_FONT_SIZE, SEX_RADIO_FRAME_COORDS
)


def validate_args() -> bool:
    pass


def clicked_generate_grid() -> None:
    pass


def create_empty_strings(main_window: Tk, rows: List[int]) -> None:
    for row in rows:
        empty_string = Label(master=main_window, text='')
        empty_string.grid(column=0, row=row)


def create_and_get_grid_size_radiobuttons():
    pass


def get_selected_sex(main_window: Tk) -> StringVar:
    return StringVar(master=main_window, value='male')  # value is default


def create_and_get_sex_radiobuttons(
    main_window: Tk, selected_sex: StringVar
) -> Tuple[Radiobutton, Radiobutton]:
    radio_frame = Frame(master=main_window)
    radio_frame.grid(**SEX_RADIO_FRAME_COORDS, sticky='W')
    radiobutton_male = Radiobutton(
        master=radio_frame, text='male', value='male',
        variable=selected_sex
    )
    radiobutton_female = Radiobutton(
        master=radio_frame, text='female', value='female',
        variable=selected_sex
    )
    radiobutton_male.grid(column=0, row=0)
    radiobutton_female.grid(column=1, row=0)
    return radiobutton_male, radiobutton_female


def get_create_button(main_window: Tk) -> Button:
    button = Button(
        master=main_window, text=CREATE_BUTTON_TITLE, width=CREATE_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR, command=clicked_generate_grid
    )
    button.grid(CREATE_BUTTON_COORDS)
    return button


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


def clicked_choose_dir(
    main_window: Tk, curr_path_label: Label,
    destination_path: str = DEFAULT_DOWNLOAD_PATH
) -> None:
    directory = filedialog.askdirectory(
        # gonna work on mac, have to check for windows and linux
        # initialdir=os.path.normpath("C://") try on Windows
        parent=main_window,  # костыль для возврата фокуса в инпут после
        initialdir=f'/Users/{getpass.getuser()}/'
    )
    if directory:
        destination_path = str(Path(directory).resolve())
    curr_path_label.configure(
        text=f'{CURR_PATH}: {destination_path}'
    )


def get_destination_button(
    main_window: Tk, current_path_label: Label, destination_path: str
) -> Button:
    button = Button(
        master=main_window, text=DESTINATION_BUTTON_TITLE,
        width=DESTINATION_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=(
            lambda
            window=main_window,
            curr_path_label=current_path_label,
            path=destination_path:
                clicked_choose_dir(
                    main_window=window,
                    curr_path_label=curr_path_label,
                    destination_path=path
                )
        )
    )
    button.grid(**DESTINATION_BUTTON_COORDS, sticky='W')
    return button


def change_text_canvas(main_canvas, text: str, main_text_id) -> None:
    # first set coords to default
    main_canvas.coords(main_text_id, 5, 5)
    main_canvas.itemconfig(
        tagOrId=main_text_id, text=text
    )


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


def get_input(main_window: Tk, row: int, column: int) -> Entry:
    nickname = Entry(master=main_window, width=20)
    nickname.grid(column=column, row=row, sticky='W')
    nickname.focus()
    return nickname


def closer(_: Event, main_window: Tk) -> None:
    main_window.destroy()


def get_window() -> Tk:
    window = Tk()

    # binds
    window.bind(
        '<Escape>',
        lambda event, main_window=window:
        closer(event, main_window=main_window)
    )

    style = Style(master=window)
    style.theme_use('aqua')
    icon = f'{os.getcwd()}/static/jordan.png'
    window.iconphoto(True, PhotoImage(file=icon))
    window.title(WINDOW_TITLE)
    window.geometry(WINDOW_SIZE)
    return window
