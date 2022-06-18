from tkinter import Button, Frame

from app.settings.ui.button import (
    BUTTON_TEXT_COLOR,
    SAVE_EVENT_NAME_BUTTON_TITLE,
    SAVE_EVENT_NAME_BUTTON_SIZE,
    SAVE_EVENT_NAME_BUTTON_COORDS
)
from apps.ui.widgets.menu.file.handlers import save_event_name


__all__ = (
    'get_save_event_name_button',
)


def get_save_event_name_button(self, frame: Frame) -> Button:
    button = Button(
        master=frame,
        width=SAVE_EVENT_NAME_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=SAVE_EVENT_NAME_BUTTON_TITLE,
        command=lambda: save_event_name(self)
    )
    button.grid(**SAVE_EVENT_NAME_BUTTON_COORDS)
    return button
