from tkinter import END, NORMAL, DISABLED

from app.ui.handlers import get_participant_fields, clean_participant_inputs
from app.ui.validators import (
    validate_input, validate_participant_exists, validate_required_field
)
from app.ui.widgets.labels import change_text_canvas


def unregister_participant(cls) -> None:
    current_tab = cls._tab_control.tab(cls._tab_control.select(), 'text')
    tab_type = cls._categories[current_tab]['type']
    fields = get_participant_fields(tab_type=tab_type)
    field_to_remove = 'nick' if tab_type == 'single' else 'crew'
    value = cls._nick.get() if tab_type == 'single' else cls._crew.get()

    if validate_participant_exists(
        cls=cls, current_tab=current_tab,
        field_to_remove=field_to_remove, value=value
    ):
        for participant in cls._categories[current_tab]['participants']:
            if participant[field_to_remove] == value:
                (
                    cls._categories[current_tab]['participants']
                    .remove(participant)
                )
                break

        cls._categories[current_tab]['text_widget'].configure(state=NORMAL)
        cls._categories[current_tab]['text_widget'].delete('1.0', END)

        for index, participant in enumerate(
            cls._categories[current_tab]['participants']
        ):
            participant_string = ', '.join(
                [participant[field] for field in fields if participant[field]]
            )
            cls._categories[current_tab]['text_widget'].insert(
                END, f'{index + 1}. {participant_string}\n'
            )

        cls._categories[current_tab]['text_widget'].configure(state=DISABLED)

        clean_participant_inputs(cls=cls, inputs=fields)

        change_text_canvas(
            canvas=cls._main_canvas, text='removed participant'
        )


def register_new_participant(cls) -> None:
    current_tab = cls._tab_control.tab(cls._tab_control.select(), 'text')
    tab_type = cls._categories[current_tab]['type']
    fields = get_participant_fields(tab_type=tab_type)
    if validate_input(cls=cls, current_tab=current_tab, tab_type=tab_type):
        participant = {'crew': cls._crew.get(), 'city': cls._city.get()}
        if tab_type == 'single':
            participant['nick'] = cls._nick.get()

        if validate_required_field(
            cls=cls, tab_type=tab_type, participant=participant
        ):
            participant = {
                field: (value if value else '')
                for field, value in participant.items()
            }

            clean_participant_inputs(cls, inputs=fields)

            cls._categories[current_tab]['participants'].append(participant)

            index = len(cls._categories[current_tab]['participants'])
            participant_string = ', '.join(
                [participant[field] for field in fields if participant[field]]
            )
            cls._categories[current_tab]['text_widget'].configure(state=NORMAL)
            cls._categories[current_tab]['text_widget'].insert(
                END, f'{index}. {participant_string}\n'
            )
            cls._categories[current_tab]['text_widget'].configure(
                state=DISABLED
            )

            change_text_canvas(
                canvas=cls._main_canvas, text='added new participant'
            )
    print('categories', cls._categories)
