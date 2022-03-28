from tkinter import Button, Frame

from app.ui.widgets.buttons.main_window_clicked import clicked_save_event_name
from settings.ui.buttons import (
    SAVE_EVENT_NAME_BUTTON_TITLE,
    BUTTON_TEXT_COLOR, SAVE_EVENT_NAME_BUTTON_COORDS,
    SAVE_EVENT_NAME_BUTTON_SIZE
)


def get_save_event_name_button(cls, frame: Frame) -> Button:
    button = Button(
        master=frame, text=SAVE_EVENT_NAME_BUTTON_TITLE,
        width=SAVE_EVENT_NAME_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_save_event_name(cls=cls)
    )
    button.grid(**SAVE_EVENT_NAME_BUTTON_COORDS)
    return button
