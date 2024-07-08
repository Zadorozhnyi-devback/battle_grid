from tkinter import Frame, Button

from app.settings.ui.button import (
    BUTTON_TEXT_COLOR,
    REGISTER_BUTTON_TITLE,
    REGISTER_BUTTON_SIZE,
    REGISTER_BUTTON_COORDS,
)
from apps.ui.widgets.tab_control.participants.handlers.register import (
    register_new_participant
)


__all__ = (
    'create_register_participant_button',
)


def create_register_participant_button(self, window: Frame) -> None:
    button = Button(
        master=window,
        width=REGISTER_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=REGISTER_BUTTON_TITLE,
        command=lambda: register_new_participant(self)
    )
    button.grid(**REGISTER_BUTTON_COORDS)
