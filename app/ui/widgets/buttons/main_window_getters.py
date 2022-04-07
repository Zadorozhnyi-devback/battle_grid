from tkinter import Button, Frame

from app.ui.widgets.buttons.main_window_clicked import clicked_save_event_name
from settings.ui.buttons import (
    BUTTON_TEXT_COLOR,
    SAVE_EVENT_NAME_BUTTON_TITLE,
    SAVE_EVENT_NAME_BUTTON_SIZE,
    SAVE_EVENT_NAME_BUTTON_COORDS
)


def get_save_event_name_button(self, frame: Frame) -> Button:
    button = Button(
        master=frame, text=SAVE_EVENT_NAME_BUTTON_TITLE,
        width=SAVE_EVENT_NAME_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_save_event_name(self=self)
    )
    button.grid(**SAVE_EVENT_NAME_BUTTON_COORDS)
    return button
