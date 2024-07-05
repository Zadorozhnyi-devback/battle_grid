from tkinter import Button, Frame

from app.settings.ui.button import (
    GENERATE_CATEGORY_GRID_BUTTON_TITLE,
    GENERATE_CATEGORY_GRID_BUTTON_SIZE,
    GENERATE_CATEGORY_GRID_BUTTON_COORDS,
    BUTTON_TEXT_COLOR
)
from apps.ui.widgets.tab_control.category_info.handlers.generate_grid import (
    generate_category_grid
)


__all__ = (
    'create_generate_category_grid_button',
)


def create_generate_category_grid_button(self, window: Frame) -> None:
    button = Button(
        master=window,
        width=GENERATE_CATEGORY_GRID_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=GENERATE_CATEGORY_GRID_BUTTON_TITLE,
        command=lambda: generate_category_grid(self)
    )
    button.grid(**GENERATE_CATEGORY_GRID_BUTTON_COORDS)
