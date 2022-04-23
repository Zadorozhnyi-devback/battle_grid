from tkinter import Button, Toplevel

from app.ui.widgets.buttons.toplevels.for_main_window.clicked import (
    clicked_save_new_event_title, clicked_add_new_category
)
from settings.ui.buttons import (BUTTON_TEXT_COLOR,
                                 ADD_CATEGORY_BUTTON_TEXT,
                                 ADD_CATEGORY_BUTTON_SIZE,
                                 ADD_CATEGORY_BUTTON_COORDS,
                                 SAVE_NEW_EVENT_TITLE_BUTTON_TITLE,
                                 SAVE_NEW_EVENT_TITLE_BUTTON_SIZE,
                                 SAVE_NEW_EVENT_TITLE_BUTTON_COORDS)


def create_add_category_button(self, frame: Toplevel) -> None:
    button = Button(
        master=frame, text=ADD_CATEGORY_BUTTON_TEXT,
        width=ADD_CATEGORY_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_add_new_category(self)
    )
    button.grid(**ADD_CATEGORY_BUTTON_COORDS)


def create_save_new_event_title_button(self, frame: Toplevel) -> None:
    button = Button(
        master=frame, text=SAVE_NEW_EVENT_TITLE_BUTTON_TITLE,
        width=SAVE_NEW_EVENT_TITLE_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_save_new_event_title(self)
    )
    button.grid(**SAVE_NEW_EVENT_TITLE_BUTTON_COORDS)
