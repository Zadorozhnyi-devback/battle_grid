from tkinter import Button, Frame

from app.ui.widgets.buttons.tab_control_clicked import register_new_participant
from settings.ui.const import (
    CREATE_BUTTON_TITLE, BUTTON_TEXT_COLOR,
    REGISTRATION_BUTTON_SIZE, REGISTRATION_BUTTON_COORDS
)


def get_registration_button(window: Frame, cls) -> Button:
    button = Button(
        master=window, text=CREATE_BUTTON_TITLE,
        width=REGISTRATION_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda c=cls: register_new_participant(cls=c)
    )
    button.grid(REGISTRATION_BUTTON_COORDS, sticky='W')
    return button
