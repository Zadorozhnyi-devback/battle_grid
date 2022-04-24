from tkinter import Event, messagebox


def main_window_closer(self) -> bool:
    answer = messagebox.askyesno(message=f'close battle grid?')
    if answer is True:
        self._window.destroy()
        return True
    else:
        self._window.focus_force()
        return False


def top_level_frame_closer(self, frame_title: str) -> None:
    getattr(self, frame_title).destroy()
    delattr(self, frame_title)
    self._window.focus_force()


def closer(_: Event, self, window_title: str) -> None:
    if window_title == '_window':  # main frame
        if main_window_closer(self) is True:
            return
    else:
        if hasattr(self, window_title):
            top_level_frame_closer(self, frame_title=window_title)
    bind_esc_for_close(self, frame_title='_window')


def press_exit_cross_signal(**kwargs) -> None:
    frame = getattr(kwargs['self'], kwargs['frame_title'])
    func = kwargs.pop('func')
    frame.protocol('WM_DELETE_WINDOW', lambda: func(**kwargs))


def bind_esc_for_close(self, frame_title: str) -> None:
    frame = getattr(self, frame_title)
    frame.bind(
        '<Escape>',
        lambda event: closer(
            event,
            self=self,
            window_title=frame_title
        )
    )
