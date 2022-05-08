from tkinter import messagebox, Toplevel

from apps.ui.widgets.buttons.toplevels.for_main_window.creators import (
    create_save_new_event_title_button
)
from apps.ui.widgets.common import create_empty_strings
from apps.ui.widgets.events import (
    press_exit_cross_signal,
    bind_esc_for_close,
    top_level_frame_closer
)
from apps.ui.widgets.inputs import get_input
from app.settings.ui.const import NEW_EVENT_TITLE_INPUT_COORDS


def clicked_create_new_event(self) -> None:
    if messagebox.askyesno(
        message='Create new event and close current window?'
    ) is True:
        self._window.destroy()
        self.__init__()
    else:
        self._window.focus_force()


def clicked_open_rename_event_frame(self) -> None:
    self._rename_window = Toplevel(master=self._window)
    self._rename_window.title(string='rename event')
    self._rename_window.resizable(False, False)

    bind_esc_for_close(self, frame_title='_rename_window')
    kwargs = {
        'self': self,
        'func': top_level_frame_closer,
        'frame_title': '_rename_window'
    }
    press_exit_cross_signal(**kwargs)

    create_empty_strings(frame=self._rename_window, rows=[1])

    self._new_event_title_input = get_input(
        frame=self._rename_window,
        **NEW_EVENT_TITLE_INPUT_COORDS
    )
    create_save_new_event_title_button(self, frame=self._rename_window)

    self._rename_window.transient(master=self._window)
    self._rename_window.grab_set()
    self._window.wait_window(window=self._rename_window)
