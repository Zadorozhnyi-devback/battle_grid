from tkinter import Button, Tk, Label, Frame

from app.ui.widgets.buttons.main_window_clicked import (
    clicked_remove_tab, clicked_add_tab,
    clicked_choose_dir, clicked_open_event
)
from settings.ui.buttons import (
    REMOVE_TAB_BUTTON_TEXT, BUTTON_TEXT_COLOR,
    REMOVE_TAB_BUTTON_SIZE, REMOVE_TAB_BUTTON_COORDS, ADD_TAB_BUTTON_TEXT,
    ADD_TAB_BUTTON_SIZE, ADD_TAB_BUTTON_COORDS, DESTINATION_BUTTON_TITLE,
    DESTINATION_BUTTON_SIZE, DESTINATION_BUTTON_COORDS,
    OPEN_EVENT_BUTTON_COORDS, OPEN_EVENT_BUTTON_SIZE,
    OPEN_EVENT_BUTTON_TEXT
)


def create_remove_tab_button(cls) -> None:
    button = Button(
        master=cls._window, text=REMOVE_TAB_BUTTON_TEXT,
        width=REMOVE_TAB_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_remove_tab(cls=cls)
    )
    button.grid(**REMOVE_TAB_BUTTON_COORDS)


def create_add_tab_button(cls) -> None:
    button = Button(
        master=cls._window, text=ADD_TAB_BUTTON_TEXT,
        width=ADD_TAB_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_add_tab(cls=cls)
    )
    button.grid(**ADD_TAB_BUTTON_COORDS)


def create_destination_button(
    main_window: Tk, current_path_label: Label, destination_path: str
) -> None:
    button = Button(
        master=main_window, text=DESTINATION_BUTTON_TITLE,
        width=DESTINATION_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=(
            lambda: clicked_choose_dir(
                main_window=main_window,
                curr_path_label=current_path_label,
                destination_path=destination_path
            )
        )
    )
    button.grid(**DESTINATION_BUTTON_COORDS)


def create_open_event_button(cls, frame: Frame) -> None:
    button = Button(
        master=frame, text=OPEN_EVENT_BUTTON_TEXT,
        width=OPEN_EVENT_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_open_event(cls=cls)
    )
    button.grid(**OPEN_EVENT_BUTTON_COORDS)
