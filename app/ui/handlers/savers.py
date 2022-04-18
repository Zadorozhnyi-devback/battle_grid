import datetime
import json

from app.ui.handlers.getters import get_serialized_categories


def save_categories(self) -> None:
    date_time = datetime.date.today().strftime('%d_%m_%y')
    path = f'events/{self._event_name}_{date_time}.json'
    categories = get_serialized_categories(categories=self._categories)
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(categories, json_file, indent=4)
