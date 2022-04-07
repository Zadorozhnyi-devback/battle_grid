from tkinter import Button, Tk, Label, Frame

from app.ui.widgets.buttons.main_window_clicked import (
    clicked_remove_category,
    clicked_choose_dir,
    clicked_open_event,
    clicked_open_add_category_toplevel
)
from settings.ui.buttons import (
    BUTTON_TEXT_COLOR,
    REMOVE_CATEGORY_BUTTON_TEXT,
    REMOVE_CATEGORY_BUTTON_SIZE,
    REMOVE_CATEGORY_BUTTON_COORDS,
    OPEN_ADD_CATEGORY_TOPLEVEL_BUTTON_TEXT,
    OPEN_ADD_CATEGORY_TOPLEVEL_BUTTON_SIZE,
    OPEN_ADD_CATEGORY_TOPLEVEL_BUTTON_COORDS,
    DESTINATION_BUTTON_TITLE,
    DESTINATION_BUTTON_SIZE,
    DESTINATION_BUTTON_COORDS,
    OPEN_EVENT_BUTTON_TEXT,
    OPEN_EVENT_BUTTON_SIZE,
    OPEN_EVENT_BUTTON_COORDS
)


def create_remove_category_button(self) -> None:
    button = Button(
        master=self._window, text=REMOVE_CATEGORY_BUTTON_TEXT,
        width=REMOVE_CATEGORY_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_remove_category(self=self)
    )
    button.grid(**REMOVE_CATEGORY_BUTTON_COORDS)


def create_open_add_category_toplevel_button(self) -> None:
    button = Button(
        master=self._window,
        text=OPEN_ADD_CATEGORY_TOPLEVEL_BUTTON_TEXT,
        width=OPEN_ADD_CATEGORY_TOPLEVEL_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_open_add_category_toplevel(self=self)
    )
    button.grid(**OPEN_ADD_CATEGORY_TOPLEVEL_BUTTON_COORDS)


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


def create_open_event_button(self, frame: Frame) -> None:
    button = Button(
        master=frame, text=OPEN_EVENT_BUTTON_TEXT,
        width=OPEN_EVENT_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_open_event(self=self)
    )
    button.grid(**OPEN_EVENT_BUTTON_COORDS)
