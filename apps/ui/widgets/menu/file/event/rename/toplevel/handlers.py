from tkinter import messagebox

from apps.ui.handlers.cleaners import remove_old_saves_if_exist
from apps.ui.handlers.savers import save_categories
from apps.ui.validators import validate_new_event_name
from apps.ui.widgets.labels.handlers import change_text_canvas


__all__ = (
    'save_new_event_title',
)


def save_new_event_title(self) -> None:
    new_event_name = self._new_event_title_input.get()
    if validate_new_event_name(self, new_event_name) is True:
        if messagebox.askyesno(
            message=f'Change {self._event_name!r} for {new_event_name!r}?'
        ) is True:
            remove_old_saves_if_exist(event_name=self._event_name)

            self._event_name = new_event_name

            change_text_canvas(
                canvas=self._event_name_title,
                text=self._event_name
            )
            self._event_name_title.config(width=120)

            save_categories(self)
        self._rename_window.destroy()
        delattr(self, '_rename_window')
        self._window.focus_force()
