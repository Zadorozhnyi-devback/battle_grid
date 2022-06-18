from tkinter import messagebox


__all__ = (
    'create_new_event'
)


def create_new_event(self) -> None:
    if messagebox.askyesno(
        message='Create new event and close current window?'
    ) is True:
        self._window.destroy()
        self.__init__()
    else:
        self._window.focus_force()
