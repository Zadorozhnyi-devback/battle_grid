from tkinter import messagebox

from app.settings.ui.fields.category_toplevel import CATEGORY_TOPLEVEL_FIELDS
from app.settings.ui.fields.main import MAIN_FIELDS
from apps.ui.handlers.cleaners import destroy_if_exists


__all__ = (
    'create_new_event'
)


def create_new_event(self) -> None:
    if messagebox.askyesno(
        message='Create new event and close current window?'
    ) is True:
        destroy_if_exists(
            self,
            fields=[*MAIN_FIELDS, *CATEGORY_TOPLEVEL_FIELDS]
        )
        self.__init__()
    else:
        self._window.focus_force()
