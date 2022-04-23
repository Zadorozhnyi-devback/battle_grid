from tkinter import messagebox

from app.ui.handlers.cleaners import remove_old_saves_if_exist
from app.ui.handlers.savers import save_categories
from app.ui.validators import (validate_new_event_name,
                               validate_create_category)
from app.ui.widgets.labels.handlers import change_text_canvas
from app.ui.widgets.windows.creators import create_new_tab


def clicked_save_new_event_title(self) -> None:
    new_event_name = self._new_event_title_input.get()
    if validate_new_event_name(self, new_event_name=new_event_name) is True:
        if messagebox.askyesno(
            message=f'Change {self._event_name!r} for {new_event_name!r}?'
        ) is True:
            remove_old_saves_if_exist(event_name=self._event_name)

            self._event_name = new_event_name

            change_text_canvas(
                canvas=self._event_name_title, text=self._event_name
            )
            self._event_name_title.config(width=120)

            save_categories(self)
        self._rename_window.destroy()
        delattr(self, '_rename_window')
        self._window.focus_force()


def clicked_add_new_category(self) -> None:
    if validate_create_category(self) is True:
        create_new_tab(self)

        self._add_category_toplevel.destroy()
        delattr(self, '_add_category_toplevel')

        self._window.focus_force()

        save_categories(self)
