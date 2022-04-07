from collections import defaultdict
from tkinter import END, Text
from typing import List, Dict, Union

from app.ui.const import BEGINNING


def get_participant_fields(tab_type: str) -> List[str]:
    fields = ['crew', 'city']
    fields.insert(BEGINNING, 'nick') if tab_type == 'single' else ...
    return fields


def get_serialized_categories(
    categories: Dict[str, Dict[str, Union[str, List[Dict[str, str]], Text]]]
) -> Dict[str, Dict[str, Union[str, List[Dict[str, str]]]]]:
    serialized_categories = defaultdict(dict)
    for cat, data in categories.items():
        for key, value in data.items():
            if key != 'text_widget':
                serialized_categories[cat][key] = value
            else:
                serialized_categories[cat][key] = value.get('1.0', END)
    return serialized_categories


def get_value_without_underscore(value: str) -> str:
    clean_value = ' '.join(value.split('_'))
    return clean_value


def get_value_with_underscore(value: str) -> str:
    value = '_'.join(value.split())
    return value
