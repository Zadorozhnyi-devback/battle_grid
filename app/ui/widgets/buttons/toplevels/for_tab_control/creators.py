from tkinter import Toplevel, Button

from app.ui.widgets.buttons.toplevels.for_tab_control.clicked import (
    clicked_save_categories
)
from settings.ui.buttons import (
    SAVE_CATEGORIES_BUTTON_COORDS, SAVE_CATEGORIES_BUTTON_SIZE,
    SAVE_CATEGORIES_BUTTON_TEXT, BUTTON_TEXT_COLOR
)


def create_save_categories_button(self, frame: Toplevel, category: str) -> None:
    button = Button(
        master=frame, text=SAVE_CATEGORIES_BUTTON_TEXT,
        width=SAVE_CATEGORIES_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_save_categories(
            self, frame=frame, category=category
        )
    )
    button.grid(**SAVE_CATEGORIES_BUTTON_COORDS)
