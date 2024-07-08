from tkinter.ttk import Style
from tkinter import PhotoImage, Tk

from apps.ui.widgets.events import (
    press_exit_cross_signal,
    main_window_closer,
    bind_esc_for_close
)


__all__ = (
    'create_window',
)


def create_window(
    self,
    title: str,
    size: str,
    icon: str = None
) -> None:
    self._window = Tk()

    # binds
    bind_esc_for_close(self, frame_title='_window')
    kwargs = {
        'self': self,
        'func': main_window_closer,
        'frame_title': '_window'
    }
    press_exit_cross_signal(**kwargs)

    style = Style(master=self._window)
    style.theme_use(themename='aqua')

    if icon is not None:
        icon = f'app/static/{icon}'
        self._window.iconphoto(True, PhotoImage(file=icon))

    self._window.title(string=title)
    self._window.geometry(newGeometry=size)
    self._window.resizable(width=False, height=False)
