from tkinter import Toplevel, Button

from app.settings.ui.button import (
    SAVE_NEW_EVENT_TITLE_BUTTON_COORDS,
    SAVE_NEW_EVENT_TITLE_BUTTON_TITLE,
    SAVE_NEW_EVENT_TITLE_BUTTON_SIZE,
    BUTTON_TEXT_COLOR
)
from .handlers import save_new_event_title


__all__ = (
    'create_save_new_event_title_button',
)


def create_save_new_event_title_button(self, frame: Toplevel) -> None:
    button = Button(
        master=frame,
        width=SAVE_NEW_EVENT_TITLE_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=SAVE_NEW_EVENT_TITLE_BUTTON_TITLE,
        command=lambda: save_new_event_title(self)
    )
    button.grid(**SAVE_NEW_EVENT_TITLE_BUTTON_COORDS)
