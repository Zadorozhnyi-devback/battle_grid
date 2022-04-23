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


def get_male_and_female_stats(self, category: str) -> Dict[str, int]:
    total = len(self._categories[category]['participants'])
    print('category', category)
    print('pidari', self._categories[category]['participants'])
    male = sum(
        participant['sex'] == 'male' for participant
        in self._categories[category]['participants']
    )
    female = sum(
        participant['sex'] == 'female' for participant
        in self._categories[category]['participants']
    )
    return {'total': total, 'male': male, 'female': female}


def get_male_and_female_stats_text(
    total: int = 0, male: int = 0, female: int = 0
) -> str:
    return (
        "participants:\n"
        "{:4}total: {}\n"
        "{:4}male: {}\n"
        "{:4}female: {}\n"
        .format('', total, '', male, '', female)
    )


def get_participant_info(
    self,
    category: str,
    fields: List[str]
) -> Dict[str, str]:
    participant = {
        field: (
            getattr(self, f'_{category}_{field}_input')
            .get()
            .capitalize()
        )
        for field in fields
    }
    if self._categories[category]['type'] == 'single':
        participant['sex'] = getattr(self, f'_{category}_selected_sex').get()
    return participant


def get_participant_string(participant: Dict[str, str]) -> str:
    return ', '.join(
        [participant[field]
         for field in participant.keys()
         if participant[field]]
    )


def get_category_info_text(self, category: str) -> str:
    stats = get_male_and_female_stats(self, category=category)
    category_info_text = get_male_and_female_stats_text(**stats)
    return category_info_text


def get_required_field(self, category: str) -> str:
    return 'nick' if self._categories[category]['type'] == 'single' else 'crew'
