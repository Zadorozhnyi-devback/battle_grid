from tkinter import Tk
from tkinter.ttk import Notebook

from settings.ui.const import (
    TAB_CONTROL_WINDOW_SIZE,
    TAB_CONTROL_WINDOW_COORDS
)


def get_tab_control(main_window: Tk) -> Notebook:
    tab_control = Notebook(master=main_window, **TAB_CONTROL_WINDOW_SIZE)
    tab_control.enable_traversal()
    tab_control.grid(**TAB_CONTROL_WINDOW_COORDS)
    return tab_control
