import os
from os import listdir
from os.path import join, isfile
from tkinter import NORMAL, END, DISABLED
from typing import List

from app.ui.const import BEGINNING
from app.ui.widgets.common import get_selected_tab_title


def clean_category_input(self) -> None:
    getattr(self, '_category_input').delete(BEGINNING, 'end')


def clean_participant_inputs(self, category: str, inputs: List[str]) -> None:
    for field in inputs:
        getattr(self, f'_{category}_{field}_input').delete(BEGINNING, 'end')


def remove_old_categories(self) -> None:
    while self._categories:
        selected_tab = self._tab_control.select()
        category = get_selected_tab_title(self=self)
        self._tab_control.forget(selected_tab)
        self._categories.pop(category)


def remove_old_saves_if_exist(event_name: str) -> None:
    event_saves = [
        obj for obj in listdir('events/')
        if (
            isfile(join('events/', obj))
            and obj.startswith(event_name)
            and obj.endswith('.json')
        )
    ]
    for event_save in event_saves:
        os.remove(f'events/{event_save}')


def clean_text_widget(self, category: str) -> None:
    self._categories[category]['text_widget'].configure(state=NORMAL)
    self._categories[category]['text_widget'].delete('1.0', END)
    self._categories[category]['text_widget'].configure(state=DISABLED)
