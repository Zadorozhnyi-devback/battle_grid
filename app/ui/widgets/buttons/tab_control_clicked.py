from typing import Dict

from app.ui.validators import validate_input_length
from app.ui.widgets.labels import change_text_canvas


def validate_required_field(cls, participant: Dict[str, str]) -> bool:
    if 'nick' in participant.keys():
        if not participant['nick']:
            change_text_canvas(
                canvas=cls._main_canvas, text="nick field can't be empty"
            )
            return False
    else:
        if not participant['crew']:
            change_text_canvas(
                canvas=cls._main_canvas, text="crew field can't be empty"
            )
        return False
    return True


def register_new_participant(cls) -> None:
    tab_control = cls._tab_control
    current_tab = cls._tab_control.tab(tab_control.select(), 'text')
    tab_type = cls._categories[current_tab]['type']
    if validate_input_length(cls=cls, tab_type=tab_type):
        participant = {'crew': cls._crew.get(), 'city': cls._city.get()}
        if tab_type == 'single':
            participant['nick'] = cls._nick.get()

        print('before', participant)
        if validate_required_field(cls=cls, participant=participant):
            participant = {
                field: (value if value else '-')
                for field, value in participant.items()
            }

            for entry in participant.keys():
                getattr(cls, f'_{entry}').delete(0, 'end')

            cls._categories[current_tab]['participants'].append(participant)

            change_text_canvas(
                canvas=cls._main_canvas, text='added new participant'
            )
    print('categories', cls._categories)
