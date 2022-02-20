import os
from tkinter import Tk, PhotoImage, Frame, Label
from tkinter.ttk import Style, Notebook

from app.ui.widgets.events import closer
from settings.ui.const import (
    WINDOW_TITLE, WINDOW_SIZE, TAB_CONTROL_WINDOW_SIZE
)


def get_tab_control(main_window: Tk) -> Notebook:
    tab_control = Notebook(master=main_window, **TAB_CONTROL_WINDOW_SIZE)
    # frame = Frame(tab_control)
    # tab_control.add(frame, text=tab_name)
    tab_control.grid(column=0, row=14, columnspan=10, sticky='W')
    # label1 = Label(frame, text='Thats first tab')
    # label1.grid(column=0, row=0)
    return tab_control


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
