from tkinter import Button, Frame

from app.settings.ui.button import (
    OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_TITLE,
    OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_SIZE,
    OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_COORDS,
    BUTTON_TEXT_COLOR
)
from apps.ui.widgets.tab_control.category_info.toplevels import (
    create_edit_category_toplevel
)


__all__ = (
    'create_edit_category_toplevel_button',
)


def create_edit_category_toplevel_button(self, window: Frame) -> None:
    button = Button(
        master=window,
        width=OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_TITLE,
        command=lambda: create_edit_category_toplevel(self)
    )
    button.grid(**OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_COORDS)
