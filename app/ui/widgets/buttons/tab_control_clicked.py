from tkinter import END, NORMAL, DISABLED

from app.ui.handlers import (
    get_participant_fields, clean_participant_inputs,
    save_category_participants
)
from app.ui.validators import (
    validate_input, validate_participant_exists, validate_required_field
)
from app.ui.widgets.labels import change_text_canvas


def unregister_participant(cls) -> None:
    category = cls._tab_control.tab(cls._tab_control.select(), 'text')
    tab_type = cls._categories[category]['type']
    fields = get_participant_fields(tab_type=tab_type)
    field_to_remove = 'nick' if tab_type == 'single' else 'crew'
    value = getattr(cls, f'_{category}_{field_to_remove}_input').get()

    if validate_participant_exists(
        cls=cls, category=category,
        field_to_remove=field_to_remove, value=value
    ):
        for participant in cls._categories[category]['participants']:
            if participant[field_to_remove] == value:
                (
                    cls._categories[category]['participants']
                    .remove(participant)
                )
                break

        cls._categories[category]['text_widget'].configure(state=NORMAL)
        cls._categories[category]['text_widget'].delete('1.0', END)

        for index, participant in enumerate(
            cls._categories[category]['participants']
        ):
            participant_string = ', '.join(
                [participant[field] for field in fields if participant[field]]
            )
            cls._categories[category]['text_widget'].insert(
                END, f'{index + 1}. {participant_string}\n'
            )

        cls._categories[category]['text_widget'].configure(state=DISABLED)

        clean_participant_inputs(cls=cls, category=category, inputs=fields)

        change_text_canvas(
            canvas=cls._main_canvas, text='removed participant'
        )
        save_category_participants(cls=cls)


def register_new_participant(cls) -> None:
    category = cls._tab_control.tab(cls._tab_control.select(), 'text')
    tab_type = cls._categories[category]['type']
    fields = get_participant_fields(tab_type=tab_type)
    if validate_input(cls=cls, category=category, tab_type=tab_type):
        participant = {
            field: getattr(cls, f'_{category}_{field}_input').get()
            for field in fields
        }
        print('categories', cls._categories)
        if validate_required_field(
            cls=cls, tab_type=tab_type, participant=participant
        ):
            clean_participant_inputs(cls=cls, category=category, inputs=fields)

            participant = {
                field: (value if value else '')
                for field, value in participant.items()
            }
            cls._categories[category]['participants'].append(participant)

            index = len(cls._categories[category]['participants'])
            participant_string = ', '.join(
                [participant[field] for field in fields if participant[field]]
            )
            cls._categories[category]['text_widget'].configure(state=NORMAL)
            cls._categories[category]['text_widget'].insert(
                END, f'{index}. {participant_string}\n'
            )
            cls._categories[category]['text_widget'].configure(state=DISABLED)

            change_text_canvas(
                canvas=cls._main_canvas, text='added new participant'
            )

            save_category_participants(cls=cls)
