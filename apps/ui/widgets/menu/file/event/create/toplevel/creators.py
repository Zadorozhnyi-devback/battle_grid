from tkinter import Toplevel, Frame

from app.settings.ui.button import EVENT_BUTTON_FRAME_COORDS
from app.settings.ui.const import (
    EVENT_NAME_CANVAS_KWARGS,
    EVENT_NAME_INPUT_COORDS,
)

from apps.ui.widgets.common import create_empty_strings
from apps.ui.widgets.inputs import get_input
from apps.ui.widgets.labels.creators import create_canvas
from .buttons import get_save_event_name_button


__all__ = (
    'create_event_toplevel',
)


def create_event_toplevel(self) -> None:
    self._event_toplevel = Toplevel(master=self._window)
    self._event_toplevel.resizable(False, False)
    self._event_toplevel.title(string='create event')

    create_canvas(frame=self._event_toplevel, **EVENT_NAME_CANVAS_KWARGS)
    self._event_name_input = get_input(
        frame=self._event_toplevel,
        **EVENT_NAME_INPUT_COORDS
    )
    self._event_name_input.focus_force()

    create_empty_strings(frame=self._event_toplevel, rows=[1])

    self._event_name_button_frame = Frame(master=self._event_toplevel)
    self._event_name_button_frame.grid(**EVENT_BUTTON_FRAME_COORDS)

    self._save_event_name_button = get_save_event_name_button(
        self,
        frame=self._event_name_button_frame
    )

    self._event_toplevel.transient(master=self._window)
    self._event_toplevel.grab_set()
    self._window.wait_window(window=self._event_toplevel)
