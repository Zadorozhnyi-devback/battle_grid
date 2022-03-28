from tkinter import Button, Frame

from app.ui.widgets.buttons.tab_control_clicked import (
    register_new_participant, unregister_participant,
    open_change_category_grid_size_frame
)
from settings.ui.buttons import (
    REGISTER_BUTTON_TITLE, UNREGISTER_BUTTON_TITLE, BUTTON_TEXT_COLOR,
    REGISTER_BUTTON_SIZE, UNREGISTER_BUTTON_SIZE, REGISTER_BUTTON_COORDS,
    UNREGISTER_BUTTON_COORDS, CHANGE_CATEGORY_GRID_BUTTON_TITLE,
    CHANGE_CATEGORY_GRID_BUTTON_SIZE, CHANGE_CATEGORY_GRID_BUTTON_COORDS
)


def create_register_participant_button(window: Frame, cls) -> None:
    button = Button(
        master=window, text=REGISTER_BUTTON_TITLE,
        width=REGISTER_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: register_new_participant(cls=cls)
    )
    button.grid(**REGISTER_BUTTON_COORDS)


def create_unregister_participant_button(window: Frame, cls) -> None:
    button = Button(
        master=window, text=UNREGISTER_BUTTON_TITLE,
        width=UNREGISTER_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: unregister_participant(cls=cls)
    )
    button.grid(**UNREGISTER_BUTTON_COORDS)


def create_change_category_grid_size_button(
    cls, window: Frame, category: str
) -> None:
    button = Button(
        master=window, text=CHANGE_CATEGORY_GRID_BUTTON_TITLE,
        width=CHANGE_CATEGORY_GRID_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: open_change_category_grid_size_frame(
            cls=cls, category=category
        )
    )
    button.grid(**CHANGE_CATEGORY_GRID_BUTTON_COORDS)
