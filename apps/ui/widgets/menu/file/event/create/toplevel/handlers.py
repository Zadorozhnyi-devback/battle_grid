import os
from tkinter import messagebox

from app.settings.ui.fields.category_toplevel import CATEGORY_TOPLEVEL_FIELDS
from app.settings.ui.fields.main import MAIN_FIELDS
from apps.ui.handlers.cleaners import destroy_if_exists


__all__ = (
    'create_new_event',
    'find_project_root'
)


def create_new_event(self) -> None:
    if messagebox.askyesno(
        message='Create new event and close current window?'
    ) is True:
        destroy_if_exists(
            self,
            fields=[*MAIN_FIELDS, *CATEGORY_TOPLEVEL_FIELDS]
        )
        entry_point_path = find_project_root()
        self.__init__(entry_point_path=entry_point_path)
    else:
        self._window.focus_force()


def find_project_root(marker_file='main.py') -> str:
    current_path = os.path.dirname(os.path.realpath(__file__))

    while True:
        if marker_file in os.listdir(current_path):
            return current_path
        parent_path = os.path.dirname(current_path)
        if parent_path == current_path:
            raise FileNotFoundError(f"Could not find the project root containing {marker_file}")
        current_path = parent_path
