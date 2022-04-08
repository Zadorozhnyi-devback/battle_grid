from tkinter import Toplevel, Button

from app.ui.widgets.buttons.toplevels.for_tab_control.clicked import (
    clicked_save_category
)
from settings.ui.buttons import (
    SAVE_CATEGORY_BUTTON_COORDS, SAVE_CATEGORY_BUTTON_SIZE,
    SAVE_CATEGORY_BUTTON_TEXT, BUTTON_TEXT_COLOR
)


def create_save_category_button(self, frame: Toplevel, category: str) -> None:
    button = Button(
        master=frame, text=SAVE_CATEGORY_BUTTON_TEXT,
        width=SAVE_CATEGORY_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_save_category(
            self=self, frame=frame, category=category
        )
    )
    button.grid(**SAVE_CATEGORY_BUTTON_COORDS)
