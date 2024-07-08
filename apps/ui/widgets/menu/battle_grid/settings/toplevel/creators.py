from tkinter import Toplevel

from app.settings.ui.fields.event_toplevel import EVENT_TOPLEVEL_FIELDS
from apps.ui.handlers.cleaners import destroy_if_exists

from .buttons import create_destination_button
from .labels import create_curr_path_label


__all__ = (
    'create_settings_toplevel',
)


def create_settings_toplevel(self) -> None:
    destroy_if_exists(self, fields=EVENT_TOPLEVEL_FIELDS)

    self._settings_toplevel = Toplevel(master=self._window)
    self._settings_toplevel.resizable(False, False)
    self._settings_toplevel.title(string='settings')
    self._settings_toplevel.geometry(newGeometry='500x300')

    create_curr_path_label(self)
    create_destination_button(self)

    self._settings_toplevel.transient(master=self._window)
    self._settings_toplevel.grab_set()
    self._window.wait_window(window=self._settings_toplevel)
