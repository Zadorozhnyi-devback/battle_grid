from tkinter import Event, messagebox


__all__ = (
    'main_window_closer',
    'top_level_closer',
    'closer',
    'press_exit_cross_signal',
    'bind_esc_for_close'
)


def main_window_closer(self, frame_title: str) -> bool:
    answer = messagebox.askyesno(message=f'close battle grid?')
    if answer is True:
        getattr(self, frame_title).destroy()
        return True
    else:
        getattr(self, frame_title).focus_force()
        return False


def top_level_closer(self, frame_title: str) -> None:
    getattr(self, frame_title).destroy()
    delattr(self, frame_title)
    self._window.focus_force()


def closer(_: Event, self, frame_title: str) -> None:
    if frame_title == '_window':  # main frame
        if main_window_closer(self, frame_title=frame_title) is True:
            return
    else:
        if hasattr(self, frame_title):
            top_level_closer(self, frame_title=frame_title)
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
            frame_title=frame_title
        )
    )
