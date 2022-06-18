from tkinter import Button, Toplevel

from app.settings.ui.button import (
    ADD_CATEGORY_BUTTON_SIZE,
    ADD_CATEGORY_BUTTON_TEXT,
    ADD_CATEGORY_BUTTON_COORDS,
    BUTTON_TEXT_COLOR
)
from apps.ui.handlers.creators import create_category


__all__ = (
    'create_add_category_button',
)


def create_add_category_button(self, frame: Toplevel) -> None:
    button = Button(
        master=frame,
        width=ADD_CATEGORY_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=ADD_CATEGORY_BUTTON_TEXT,
        command=lambda: create_category(self)
    )
    button.grid(**ADD_CATEGORY_BUTTON_COORDS)
