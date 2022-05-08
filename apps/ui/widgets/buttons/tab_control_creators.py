from tkinter import Button, Frame

from apps.ui.widgets.buttons.tab_control_clicked import (
    clicked_register_new_participant,
    clicked_unregister_participant,
    clicked_open_edit_category_toplevel
)
from app.settings.ui.buttons import (
    BUTTON_TEXT_COLOR,
    REGISTER_BUTTON_TITLE,
    REGISTER_BUTTON_SIZE,
    REGISTER_BUTTON_COORDS,
    UNREGISTER_BUTTON_TITLE,
    UNREGISTER_BUTTON_SIZE,
    UNREGISTER_BUTTON_COORDS,
    OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_TITLE,
    OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_SIZE,
    OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_COORDS
)


def create_register_participant_button(self, window: Frame) -> None:
    button = Button(
        master=window,
        width=REGISTER_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=REGISTER_BUTTON_TITLE,
        command=lambda: clicked_register_new_participant(self)
    )
    button.grid(**REGISTER_BUTTON_COORDS)


def create_unregister_participant_button(self, window: Frame) -> None:
    button = Button(
        master=window,
        width=UNREGISTER_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=UNREGISTER_BUTTON_TITLE,
        command=lambda: clicked_unregister_participant(self)
    )
    button.grid(**UNREGISTER_BUTTON_COORDS)


def create_open_edit_category_toplevel_button(self, window: Frame) -> None:
    button = Button(
        master=window,
        width=OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_TITLE,
        command=lambda: clicked_open_edit_category_toplevel(self)
    )
    button.grid(**OPEN_EDIT_CATEGORY_TOPLEVEL_BUTTON_COORDS)
