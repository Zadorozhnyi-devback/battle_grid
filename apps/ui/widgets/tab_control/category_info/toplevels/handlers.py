from tkinter import Toplevel

from apps.ui.handlers.updators import update_category_data
from apps.ui.validators import validate_for_update_category


__all__ = (
    'save_categories',
)


def save_categories(self, frame: Toplevel, category: str) -> None:
    if validate_for_update_category(self, category) is True:
        update_category_data(self, category)
        delattr(self, f'_{category}_toplevel_frame')

    delattr(self, '_category_input')
    frame.destroy()
    self._window.focus_force()
