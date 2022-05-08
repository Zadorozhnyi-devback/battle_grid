from tkinter import Toplevel, Button

from apps.ui.widgets.buttons.toplevels.for_tab_control.clicked import (
    clicked_save_categories
)
from app.settings.ui.buttons import (
    BUTTON_TEXT_COLOR,
    SAVE_CATEGORIES_BUTTON_COORDS,
    SAVE_CATEGORIES_BUTTON_SIZE,
    SAVE_CATEGORIES_BUTTON_TEXT
)


def create_save_categories_button(
    self,
    frame: Toplevel,
    category: str
) -> None:
    button = Button(
        master=frame,
        width=SAVE_CATEGORIES_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=SAVE_CATEGORIES_BUTTON_TEXT,
        command=lambda: clicked_save_categories(
            self,
            frame=frame,
            category=category
        )
    )
    button.grid(**SAVE_CATEGORIES_BUTTON_COORDS)
