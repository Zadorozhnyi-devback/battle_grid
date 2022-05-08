from tkinter import Button, Frame

from apps.ui.widgets.buttons.main_window_clicked import clicked_save_event_name
from app.settings.ui.buttons import (
    BUTTON_TEXT_COLOR,
    SAVE_EVENT_NAME_BUTTON_TITLE,
    SAVE_EVENT_NAME_BUTTON_SIZE,
    SAVE_EVENT_NAME_BUTTON_COORDS
)


def get_save_event_name_button(self, frame: Frame) -> Button:
    button = Button(
        master=frame,
        width=SAVE_EVENT_NAME_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=SAVE_EVENT_NAME_BUTTON_TITLE,
        command=lambda: clicked_save_event_name(self)
    )
    button.grid(**SAVE_EVENT_NAME_BUTTON_COORDS)
    return button
