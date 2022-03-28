from tkinter import Event, Tk, messagebox, Toplevel
from typing import Union


def main_window_closer(cls, frame: Tk) -> bool:
    answer = messagebox.askyesno(message=f"close battle grid?")
    if answer is True:
        frame.destroy()
        return True
    else:
        cls._window.focus_force()
        return False


def closer(
    _: Event, cls, frame: Union[Tk, Toplevel], window_title: str
) -> None:
    if window_title == '_window':
        if main_window_closer(cls=cls, frame=frame) is True:
            return
    else:
        if hasattr(cls, window_title):
            getattr(cls, window_title).destroy()
            delattr(cls, window_title)
            cls._window.focus_force()
    bind_esc_for_close(cls=cls, frame=cls._window, window_title='_window')


def bind_esc_for_close(
    cls, window_title: str, frame: Union[Tk, Toplevel]
) -> None:
    frame.bind(
        '<Escape>', lambda event: closer(
            _=event, cls=cls, frame=frame, window_title=window_title
        )
    )
