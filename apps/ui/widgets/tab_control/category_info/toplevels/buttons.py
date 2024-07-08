from tkinter import Button, Toplevel


from app.settings.ui.button import (
    SAVE_CATEGORIES_BUTTON_COORDS,
    SAVE_CATEGORIES_BUTTON_SIZE,
    SAVE_CATEGORIES_BUTTON_TEXT,
    BUTTON_TEXT_COLOR
)
from .handlers import save_categories


__all__ = (
    'create_save_categories_button',
)


def create_save_categories_button(
    self,
    frame: Toplevel,
    category: str
) -> None:
    button = Button(
        master=frame,
        width=SAVE_CATEGORIES_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=SAVE_CATEGORIES_BUTTON_TEXT,
        command=lambda: save_categories(
            self,
            frame=frame,
            category=category
        )
    )
    button.grid(**SAVE_CATEGORIES_BUTTON_COORDS)
