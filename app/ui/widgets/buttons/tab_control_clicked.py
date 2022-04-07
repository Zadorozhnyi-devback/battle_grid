from tkinter import END, NORMAL, DISABLED, Toplevel

from app.ui.const import BEGINNING
from app.ui.handlers.cleaners import (
    clean_participant_inputs, remove_old_saves_if_exist
)
from app.ui.handlers.getters import get_participant_fields
from app.ui.handlers.savers import save_category_participants
from app.ui.validators import (
    validate_participant_inputs, validate_participant_exists,
    validate_participant_required_field, validate_event_name_exists
)
from app.ui.widgets.buttons.toplevels.for_tab_control.creators import (
    create_save_category_button
)
from app.ui.widgets.common import create_empty_strings, get_selected_tab_title
from app.ui.widgets.events import (
    bind_esc_for_close, press_exit_cross_signal, top_level_frame_closer
)
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels.creators import create_canvas
from app.ui.widgets.labels.handlers import change_text_canvas
from app.ui.widgets.radio import (
    create_grid_size_radio, create_category_type_radio
)
from settings.ui.const import (
    CATEGORY_TITLE_INPUT_COORDS, CATEGORY_CANVAS_KWARGS,
    GRID_SIZE_CANVAS_KWARGS
)


def clicked_open_edit_category_toplevel(self) -> None:
    if validate_event_name_exists(self=self) is True:
        category_frame_window = Toplevel(master=self._window)
        category_frame_window.focus_force()
        category_frame_window.resizable(False, False)

        self._category_input = get_input(
            frame=category_frame_window, **CATEGORY_TITLE_INPUT_COORDS
        )

        create_canvas(frame=category_frame_window, **CATEGORY_CANVAS_KWARGS)

        category = get_selected_tab_title(self=self)
        category_frame = f'_{category}_toplevel_frame'
        self._category_input.insert(BEGINNING, category)
        self._selected_category_type.set(self._categories[category]['type'])
        self._selected_grid_size.set(self._categories[category]['grid_size'])
        if not self._categories[category]['participants']:
            create_category_type_radio(
                frame=category_frame_window,
                selected_type=self._selected_category_type
            )
        create_save_category_button(
            self=self, frame=category_frame_window, category=category
        )

        category_frame_window.title(string='edit category')
        setattr(self, category_frame, category_frame_window)

        bind_esc_for_close(self=self, frame_title=category_frame)
        kwargs = {
            'self': self, 'func': top_level_frame_closer,
            'frame_title': category_frame
        }
        press_exit_cross_signal(**kwargs)

        create_empty_strings(frame=category_frame_window, rows=[2, 4])

        create_grid_size_radio(
            window=category_frame_window,
            selected_size=self._selected_grid_size
        )
        create_canvas(frame=category_frame_window, **GRID_SIZE_CANVAS_KWARGS)

        category_frame_window.transient(master=self._window)
        category_frame_window.grab_set()
        self._window.wait_window(window=category_frame_window)


def unregister_participant(self) -> None:
    category = get_selected_tab_title(self=self)
    tab_type = self._categories[category]['type']
    fields = get_participant_fields(tab_type=tab_type)
    field_to_remove = 'nick' if tab_type == 'single' else 'crew'
    value = getattr(self, f'_{category}_{field_to_remove}_input').get()

    if validate_participant_exists(
        self=self, category=category,
        field_to_remove=field_to_remove, value=value
    ):
        for participant in self._categories[category]['participants']:
            if participant[field_to_remove] == value:
                (
                    self._categories[category]['participants']
                    .remove(participant)
                )
                break

        self._categories[category]['text_widget'].configure(state=NORMAL)
        self._categories[category]['text_widget'].delete('1.0', END)

        for index, participant in enumerate(
            self._categories[category]['participants']
        ):
            participant_string = ', '.join(
                [participant[field] for field in fields if participant[field]]
            )
            self._categories[category]['text_widget'].insert(
                END, f'{index + 1}. {participant_string}\n'
            )

        self._categories[category]['text_widget'].configure(state=DISABLED)

        clean_participant_inputs(self=self, category=category, inputs=fields)

        change_text_canvas(
            canvas=self._main_canvas, text='removed participant'
        )
        save_category_participants(self=self)


def register_new_participant(self) -> None:
    category = get_selected_tab_title(self=self)
    tab_type = self._categories[category]['type']
    fields = get_participant_fields(tab_type=tab_type)
    if validate_participant_inputs(
        self=self, category=category, tab_type=tab_type
    ) is True:
        participant = {
            field: getattr(
                self, f'_{category}_{field}_input'
            ).get().capitalize()
            for field in fields
        }
        print('categories', self._categories)
        if validate_participant_required_field(
            self=self, tab_type=tab_type, participant=participant
        ) is True:
            clean_participant_inputs(
                self=self, category=category, inputs=fields
            )

            participant = {
                field: (value if value else '')
                for field, value in participant.items()
            }
            self._categories[category]['participants'].append(participant)
            print('participants', self._categories[category]['participants'])
            print('participant', participant)
            index = len(self._categories[category]['participants'])
            participant_string = ', '.join(
                [participant[field] for field in fields if participant[field]]
            )
            self._categories[category]['text_widget'].configure(state=NORMAL)
            self._categories[category]['text_widget'].insert(
                END, f'{index}. {participant_string}\n'
            )
            self._categories[category]['text_widget'].configure(state=DISABLED)

            change_text_canvas(
                canvas=self._main_canvas, text='added new participant'
            )

            remove_old_saves_if_exist(event_name=self._event_name)
            save_category_participants(self=self)
