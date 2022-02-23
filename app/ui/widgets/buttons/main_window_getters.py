from tkinter import Button, Tk, Label

from app.ui.widgets.buttons.main_window_clicked import (
    clicked_remove_tab, clicked_add_tab, clicked_choose_dir
)
from settings.ui.const import (
    REMOVE_TAB_BUTTON_TEXT, BUTTON_TEXT_COLOR,
    REMOVE_TAB_BUTTON_SIZE, REMOVE_TAB_BUTTON_COORDS, ADD_TAB_BUTTON_TEXT,
    ADD_TAB_BUTTON_SIZE, ADD_TAB_BUTTON_COORDS, DESTINATION_BUTTON_TITLE,
    DESTINATION_BUTTON_SIZE, DESTINATION_BUTTON_COORDS
)


def get_remove_tab_button(cls) -> Button:
    button = Button(
        master=cls._window, text=REMOVE_TAB_BUTTON_TEXT,
        width=REMOVE_TAB_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda c=cls: clicked_remove_tab(cls=c)
    )
    button.grid(REMOVE_TAB_BUTTON_COORDS)
    return button


def get_add_tab_button(cls) -> Button:
    button = Button(
        master=cls._window, text=ADD_TAB_BUTTON_TEXT,
        width=ADD_TAB_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda c=cls: clicked_add_tab(cls=c)
    )
    button.grid(ADD_TAB_BUTTON_COORDS)
    return button


def get_destination_button(
    main_window: Tk, current_path_label: Label, destination_path: str
) -> Button:
    button = Button(
        master=main_window, text=DESTINATION_BUTTON_TITLE,
        width=DESTINATION_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=(
            lambda
            window=main_window,
            curr_path_label=current_path_label,
            path=destination_path:
                clicked_choose_dir(
                    main_window=window,
                    curr_path_label=curr_path_label,
                    destination_path=path
                )
        )
    )
    button.grid(**DESTINATION_BUTTON_COORDS, sticky='W')
    return button
