from tkinter import Toplevel

from app.ui.handlers.updators import update_category_data
from app.ui.validators import validate_update_category


def clicked_save_categories(self, frame: Toplevel, category: str) -> None:
    if validate_update_category(self) is True:
        update_category_data(self, category=category)
        delattr(self, f'_{category}_toplevel_frame')

    delattr(self, '_category_input')
    frame.destroy()
    self._window.focus_force()
