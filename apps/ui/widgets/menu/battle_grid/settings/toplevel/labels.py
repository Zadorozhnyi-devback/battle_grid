from tkinter import Label

from app.settings.ui.const import (
    CURR_PATH_LABEL_COORDS,
    CURRENT_PATH,
    DEFAULT_FONT_SIZE,
    ARIAL_BOLD
)


__all__ = (
    'create_curr_path_label',
)


def create_curr_path_label(self) -> None:
    path = self._destination_path.split('/')[-1]
    curr_path_label = Label(
        master=self._settings_toplevel,
        font=(ARIAL_BOLD, DEFAULT_FONT_SIZE),
        text=f'{CURRENT_PATH}: {path}'
    )
    curr_path_label.grid(**CURR_PATH_LABEL_COORDS)
