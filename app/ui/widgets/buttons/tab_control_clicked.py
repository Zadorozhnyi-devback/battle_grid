from tkinter import END, NORMAL, DISABLED, Toplevel

from app.ui.handlers import (
    get_participant_fields, clean_participant_inputs,
    save_category_participants, remove_old_saves_if_exist
)
from app.ui.validators import (
    validate_input, validate_participant_exists, validate_required_field
)
from app.ui.widgets.buttons.after_click_creators import (
    create_save_new_category_grid_size_button
)

from app.ui.widgets.common import create_empty_strings
from app.ui.widgets.events import bind_esc_for_close
from app.ui.widgets.labels import change_text_canvas
from app.ui.widgets.radio import create_grid_size_radio
from settings.ui.const import CHANGE_GRID_SIZE_RADIO_FRAME_COORDS


def open_change_category_grid_size_frame(cls, category: str) -> None:
    setattr(
        cls,
        f'_{category}_change_grid_window',
        Toplevel(master=cls._window)
    )
    change_grid_window = getattr(cls, f'_{category}_change_grid_window')
    change_grid_window.title(string='change grid')
    change_grid_window.focus_force()
    change_grid_window.resizable(False, False)

    bind_esc_for_close(
        cls=cls, frame=change_grid_window,
        window_title=f'_{category}_change_grid_window'
    )

    create_empty_strings(window=change_grid_window, rows=[1])

    create_grid_size_radio(
        window=change_grid_window,
        selected_size=cls._selected_grid_size,
        coords=CHANGE_GRID_SIZE_RADIO_FRAME_COORDS
    )

    create_save_new_category_grid_size_button(
        cls=cls, frame=change_grid_window, category=category
    )

    change_grid_window.transient(master=cls._window)
    change_grid_window.grab_set()
    cls._window.wait_window(window=change_grid_window)


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
            field: getattr(
                cls, f'_{category}_{field}_input'
            ).get().capitalize()
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
            print('participants', cls._categories[category]['participants'])
            print('participant', participant)
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

            remove_old_saves_if_exist(event_name=cls._event_name)
            save_category_participants(cls=cls)
