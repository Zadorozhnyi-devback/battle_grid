from tkinter import Frame, Button

from app.settings.ui.button import (
    BUTTON_TEXT_COLOR,
    UNREGISTER_BUTTON_TITLE,
    UNREGISTER_BUTTON_SIZE,
    UNREGISTER_BUTTON_COORDS
)
from apps.ui.widgets.tab_control.participants.handlers.unregister import (
    unregister_participant
)


__all__ = (
    'create_unregister_participant_button',
)


def create_unregister_participant_button(self, window: Frame) -> None:
    button = Button(
        master=window,
        width=UNREGISTER_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        text=UNREGISTER_BUTTON_TITLE,
        command=lambda: unregister_participant(self)
    )
    button.grid(**UNREGISTER_BUTTON_COORDS)
