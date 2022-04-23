from tkinter import Scrollbar, Frame, Text, NONE, DISABLED

from settings.ui.const import SCROLLBAR_KWARGS, TEXT_WINDOW_KWARGS, HELVETICA


def get_category_people_list(tab_frame: Frame) -> Text:
    scrollbar = Scrollbar(master=tab_frame)
    scrollbar.grid(**SCROLLBAR_KWARGS)

    text = Text(
        master=tab_frame,
        width=48, heigh=18.5,
        yscrollcommand=scrollbar.set, wrap=NONE,
        font=(HELVETICA, 13), state=DISABLED
    )
    text.grid(**TEXT_WINDOW_KWARGS)

    scrollbar.config(command=text.yview)
    tab_frame.columnconfigure(2, weight=1)
    return text
