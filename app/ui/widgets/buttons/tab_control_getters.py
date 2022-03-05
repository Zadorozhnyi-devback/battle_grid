from tkinter import Button, Frame

from app.ui.widgets.buttons.tab_control_clicked import (
    register_new_participant, unregister_participant
)
from settings.ui.const import (
    REGISTER_BUTTON_TITLE, UNREGISTER_BUTTON_TITLE, BUTTON_TEXT_COLOR,
    REGISTER_BUTTON_SIZE, UNREGISTER_BUTTON_SIZE, REGISTER_BUTTON_COORDS,
    UNREGISTER_BUTTON_COORDS
)


def get_register_button(window: Frame, cls) -> Button:
    button = Button(
        master=window, text=REGISTER_BUTTON_TITLE,
        width=REGISTER_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda c=cls: register_new_participant(cls=c)
    )
    button.grid(REGISTER_BUTTON_COORDS, sticky='W')
    return button


def get_unregister_button(window: Frame, cls) -> Button:
    button = Button(
        master=window, text=UNREGISTER_BUTTON_TITLE,
        width=UNREGISTER_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda c=cls: unregister_participant(cls=c)
    )
    button.grid(UNREGISTER_BUTTON_COORDS, sticky='W')
    return button
