from tkinter import Button, Tk, messagebox

from settings.ui.const import (
    CREATE_NEW_EVENT_BUTTON_TITLE, BUTTON_TEXT_COLOR,
    CREATE_NEW_EVENT_NAME_BUTTON_COORDS, CREATE_NEW_EVENT_BUTTON_SIZE
)


def clicked_create_new_event(cls) -> None:
    if messagebox.askyesno(
        message="Create new event and close current window?"
    ):
        cls._window.destroy()
        cls.__init__()


def get_create_new_event_button(cls, main_window: Tk) -> Button:
    button = Button(
        master=main_window, text=CREATE_NEW_EVENT_BUTTON_TITLE,
        width=CREATE_NEW_EVENT_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda c=cls: clicked_create_new_event(cls=c)
    )
    button.grid(**CREATE_NEW_EVENT_NAME_BUTTON_COORDS, sticky='W')
    return button
