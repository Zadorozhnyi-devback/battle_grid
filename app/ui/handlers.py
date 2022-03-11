import datetime
import json
from collections import defaultdict
from tkinter import Text, END
from typing import List, Dict, Union

from app.ui.const import BEGINNING
from app.ui.widgets.common import get_selected_tab_title


def get_participant_fields(tab_type: str) -> List[str]:
    fields = ['crew', 'city']
    fields.insert(BEGINNING, 'nick') if tab_type == 'single' else ...
    return fields


def clean_category_input(cls) -> None:
    getattr(cls, '_category_input').delete(BEGINNING, 'end')


def clean_participant_inputs(cls, category: str, inputs: List[str]) -> None:
    for field in inputs:
        getattr(cls, f'_{category}_{field}_input').delete(BEGINNING, 'end')


def remove_old_categories(cls) -> None:
    while cls._categories:
        selected_tab = cls._tab_control.select()
        category = get_selected_tab_title(cls=cls)
        cls._tab_control.forget(selected_tab)
        cls._categories.pop(category)


def get_serialized_categories(
    categories: Dict[str, Dict[str, Union[str, List[Dict[str, str]], Text]]]
) -> Dict[str, Dict[str, Union[str, List[Dict[str, str]]]]]:
    serialized_categories = defaultdict(dict)
    for k, v in categories.items():
        for key, value in v.items():
            if key != 'text_widget':
                serialized_categories[k][key] = value
            else:
                serialized_categories[k][key] = value.get('1.0', END)
    return serialized_categories


def save_category_participants(cls):
    date_time = datetime.date.today().strftime('%d_%m_%y')
    path = f'events/{cls._event_name}_{date_time}.json'
    categories = get_serialized_categories(categories=cls._categories)
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(categories, json_file, indent=4)
