from tkinter import Button

from app.settings.ui.button import (
    DESTINATION_BUTTON_SIZE,
    BUTTON_TEXT_COLOR,
    DESTINATION_BUTTON_TITLE,
    DESTINATION_BUTTON_COORDS
)

from .handlers import clicked_choose_dir


__all__ = (
    'create_destination_button',
)


def create_destination_button(self) -> None:
    button = Button(
        master=self._settings_toplevel,
        width=DESTINATION_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=DESTINATION_BUTTON_TITLE,
        command=lambda: clicked_choose_dir(self)
    )
    button.grid(**DESTINATION_BUTTON_COORDS)
