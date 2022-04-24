from tkinter import Button, Frame

from app.ui.widgets.buttons.after_click_clicked import (
    clicked_create_new_event,
    clicked_open_rename_event_frame
)

from settings.ui.buttons import (
    BUTTON_TEXT_COLOR,
    CREATE_NEW_EVENT_BUTTON_TITLE,
    CREATE_NEW_EVENT_BUTTON_SIZE,
    CREATE_NEW_EVENT_NAME_BUTTON_COORDS,
    RENAME_EVENT_BUTTON_TEXT,
    RENAME_EVENT_BUTTON_SIZE,
    RENAME_EVENT_BUTTON_COORDS
)


def create_make_new_event_button(self, frame: Frame) -> None:
    button = Button(
        master=frame,
        width=CREATE_NEW_EVENT_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=CREATE_NEW_EVENT_BUTTON_TITLE,
        command=lambda: clicked_create_new_event(self)
    )
    button.grid(**CREATE_NEW_EVENT_NAME_BUTTON_COORDS)


def create_rename_event_button(self, frame: Frame) -> None:
    button = Button(
        master=frame,
        width=RENAME_EVENT_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=RENAME_EVENT_BUTTON_TEXT,
        command=lambda: clicked_open_rename_event_frame(self)
    )
    button.grid(**RENAME_EVENT_BUTTON_COORDS)
