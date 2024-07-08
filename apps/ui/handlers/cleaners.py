import os
from os import listdir
from os.path import join, isfile
from tkinter import NORMAL, END, DISABLED, TclError, messagebox
from typing import List

from apps.ui.const import BEGINNING
from apps.ui.handlers.getters import get_text_widget
from apps.ui.handlers.savers import save_categories
from apps.ui.widgets.labels.handlers import change_text_canvas
from apps.ui.widgets.tab_control.utils.common import get_selected_tab_title
from shared.utils import update_timestamp


__all__ = (
    'clean_category_input',
    'clean_participant_inputs',
    'remove_category',
    'remove_old_categories',
    'remove_old_saves_if_exist',
    'clean_text_widget',
    'destroy_if_exists'
)


def clean_category_input(self) -> None:
    getattr(self, '_category_input').delete(BEGINNING, 'end')


def clean_participant_inputs(self, category: str, inputs: List[str]) -> None:
    for field in inputs:
        getattr(self, f'_{category}_{field}_input').delete(BEGINNING, 'end')


def remove_old_categories(self) -> None:
    while self._categories:
        selected_tab = self._tab_control.select()
        category = get_selected_tab_title(self)
        self._tab_control.forget(selected_tab)
        self._categories.pop(category)


def remove_category(self) -> None:
    selected_tab = self._tab_control.select()
    category = get_selected_tab_title(self)
    if category:
        answer = messagebox.askyesno(
            message=f'delete category {category!r}?'
        )
        if answer is True:
            self._tab_control.forget(selected_tab)
            self._categories.pop(category)

            update_timestamp(self, category=category)

            remove_old_saves_if_exist(event_name=self._event_name)
            save_categories(self)
    else:
        change_text_canvas(
            canvas=self._main_canvas,
            text='no categories to remove'
        )


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
    text_widget = get_text_widget(self, category)
    text_widget.configure(state=NORMAL)
    text_widget.delete('1.0', END)
    text_widget.configure(state=DISABLED)


def destroy_if_exists(self, fields: List[str]) -> None:
    for field in fields:
        if hasattr(self, field):
            try:
                getattr(self, field).destroy()
            except TclError:
                pass
            delattr(self, field)
