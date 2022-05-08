from tkinter import Button, Toplevel

from apps.ui.widgets.buttons.toplevels.for_main_window.clicked import (
    clicked_save_new_event_title,
    clicked_add_new_category
)
from app.settings.ui.buttons import (
    BUTTON_TEXT_COLOR,
    ADD_CATEGORY_BUTTON_TEXT,
    ADD_CATEGORY_BUTTON_SIZE,
    ADD_CATEGORY_BUTTON_COORDS,
    SAVE_NEW_EVENT_TITLE_BUTTON_TITLE,
    SAVE_NEW_EVENT_TITLE_BUTTON_SIZE,
    SAVE_NEW_EVENT_TITLE_BUTTON_COORDS
)


def create_add_category_button(self, frame: Toplevel) -> None:
    button = Button(
        master=frame,
        width=ADD_CATEGORY_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=ADD_CATEGORY_BUTTON_TEXT,
        command=lambda: clicked_add_new_category(self)
    )
    button.grid(**ADD_CATEGORY_BUTTON_COORDS)


def create_save_new_event_title_button(self, frame: Toplevel) -> None:
    button = Button(
        master=frame,
        width=SAVE_NEW_EVENT_TITLE_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=SAVE_NEW_EVENT_TITLE_BUTTON_TITLE,
        command=lambda: clicked_save_new_event_title(self)
    )
    button.grid(**SAVE_NEW_EVENT_TITLE_BUTTON_COORDS)
