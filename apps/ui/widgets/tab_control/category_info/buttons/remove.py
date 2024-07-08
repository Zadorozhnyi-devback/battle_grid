from tkinter import Button

from apps.ui.handlers.cleaners import remove_category

from app.settings.ui.button import (
    BUTTON_TEXT_COLOR,
    REMOVE_CATEGORY_BUTTON_SIZE,
    REMOVE_CATEGORY_BUTTON_TEXT,
    REMOVE_CATEGORY_BUTTON_COORDS
)


__all__ = (
    'create_remove_category_button'
)


def create_remove_category_button(self) -> None:
    button = Button(
        master=self._window,
        width=REMOVE_CATEGORY_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=REMOVE_CATEGORY_BUTTON_TEXT,
        command=lambda: remove_category(self)
    )
    button.grid(**REMOVE_CATEGORY_BUTTON_COORDS)
