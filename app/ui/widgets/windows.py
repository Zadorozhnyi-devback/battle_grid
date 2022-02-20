import os
from tkinter import Tk, PhotoImage
from tkinter.ttk import Style, Notebook

from app.ui.widgets.events import closer
from settings.ui.const import (
    WINDOW_TITLE, WINDOW_SIZE, TAB_CONTROL_WINDOW_SIZE
)


def get_tab_control(main_window: Tk) -> Notebook:
    tab_control = Notebook(master=main_window, **TAB_CONTROL_WINDOW_SIZE)
    tab_control.grid(column=0, row=14, columnspan=10, sticky='W')
    return tab_control


def get_window() -> Tk:
    window = Tk()

    # binds
    window.bind(
        '<Escape>',
        lambda event, w=window: closer(event, main_window=w)
    )

    style = Style(master=window)
    style.theme_use('aqua')
    icon = f'{os.getcwd()}/static/jordan.png'
    window.iconphoto(True, PhotoImage(file=icon))
    window.title(WINDOW_TITLE)
    window.geometry(WINDOW_SIZE)
    return window
