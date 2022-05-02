from tkinter import Toplevel

from app.ui.const import BEGINNING
from app.ui.handlers.cleaners import (
    clean_participant_inputs,
    remove_old_saves_if_exist,
    clean_text_widget
)
from app.ui.handlers.getters import (
    get_participant_fields,
    get_participant_info,
    get_participant_string,
    get_category_info_text,
    get_category_type,
    get_required_field,
    get_amount_of_category_participants,
    get_grid_size,
    get_participants,
    get_input_value,
)
from app.ui.handlers.savers import save_categories
from app.ui.handlers.updators import (
    add_new_participant_in_text_widget,
    update_category_sex_stats_canvas
)
from app.ui.validators import (
    validate_participant_inputs,
    validate_participant_exists,
    validate_event_name_exists
)
from app.ui.widgets.buttons.toplevels.for_tab_control.creators import (
    create_save_categories_button
)
from app.ui.widgets.common import (
    create_empty_strings,
    get_selected_tab_title
)
from app.ui.widgets.events import (
    bind_esc_for_close,
    press_exit_cross_signal,
    top_level_frame_closer
)
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels.creators import create_canvas
from app.ui.widgets.labels.handlers import change_text_canvas
from app.ui.widgets.radio import (
    create_grid_size_radio,
    create_category_type_radio
)
from settings.ui.const import (
    CATEGORY_TITLE_INPUT_COORDS,
    CATEGORY_CANVAS_KWARGS,
    GRID_SIZE_CANVAS_KWARGS
)


def clicked_open_edit_category_toplevel(self) -> None:
    if validate_event_name_exists(self) is True:
        category_frame_window = Toplevel(master=self._window)
        category_frame_window.focus_force()
        category_frame_window.resizable(False, False)

        self._category_input = get_input(
            frame=category_frame_window,
            **CATEGORY_TITLE_INPUT_COORDS
        )

        create_canvas(frame=category_frame_window, **CATEGORY_CANVAS_KWARGS)

        category = get_selected_tab_title(self)
        category_frame = f'_{category}_toplevel_frame'

        self._category_input.insert(BEGINNING, category)
        self._selected_category_type.set(get_category_type(self, category))
        self._selected_grid_size.set(get_grid_size(self, category))

        if not self._categories[category]['participants']:
            create_category_type_radio(
                frame=category_frame_window,
                selected_type=self._selected_category_type
            )

        create_empty_strings(frame=category_frame_window, rows=[2, 4])

        create_grid_size_radio(
            self,
            window=category_frame_window,
            selected_size=self._selected_grid_size,
            category=category
        )
        create_canvas(frame=category_frame_window, **GRID_SIZE_CANVAS_KWARGS)

        create_save_categories_button(
            self,
            frame=category_frame_window,
            category=category
        )

        category_frame_window.title(string='edit category')
        setattr(self, category_frame, category_frame_window)

        bind_esc_for_close(self, frame_title=category_frame)
        kwargs = {
            'self': self,
            'func': top_level_frame_closer,
            'frame_title': category_frame
        }
        press_exit_cross_signal(**kwargs)

        category_frame_window.transient(master=self._window)
        category_frame_window.grab_set()
        self._window.wait_window(window=category_frame_window)


def unregister_participant(self) -> None:
    category = get_selected_tab_title(self)
    category_type = get_category_type(self, category)
    fields = get_participant_fields(tab_type=category_type)
    required_field = get_required_field(self, category=category)
    value = get_input_value(self, category, required_field)

    if validate_participant_exists(
        self,
        category=category,
        required_field=required_field,
        value=value
    ) is True:
        participants = get_participants(self, category)
        for participant in participants:
            if participant[required_field] == value:
                participants.remove(participant)
                break

        clean_text_widget(self, category=category)

        for index, p in enumerate(participants, start=1):
            participant_string = get_participant_string(participant=p)

            add_new_participant_in_text_widget(
                self,
                participant_string=participant_string,
                category=category,
                index=index
            )

        if get_category_type(self, category) == 'single':
            category_info_text = get_category_info_text(self, category)
            update_category_sex_stats_canvas(
                self,
                category=category,
                category_info_text=category_info_text
            )

        change_text_canvas(
            canvas=self._main_canvas,
            text=f'removed participant {value!r}'
        )

        clean_participant_inputs(self, category=category, inputs=fields)
        remove_old_saves_if_exist(event_name=self._event_name)
        save_categories(self)


def register_new_participant(self) -> None:
    category = get_selected_tab_title(self)
    category_type = get_category_type(self, category)
    fields = get_participant_fields(tab_type=category_type)

    if validate_participant_inputs(
        self,
        category=category,
        tab_type=category_type
    ) is True:
        participant = get_participant_info(
            self,
            category=category,
            fields=fields
        )

        self._categories[category]['participants'].append(participant)

        participant_string = get_participant_string(participant=participant)
        index = get_amount_of_category_participants(self, category)
        add_new_participant_in_text_widget(
            self,
            participant_string=participant_string,
            category=category,
            index=index
        )

        if get_category_type(self, category) == 'single':
            category_info_text = get_category_info_text(self, category)
            update_category_sex_stats_canvas(
                self,
                category=category,
                category_info_text=category_info_text
            )

        required_field = get_required_field(self, category=category)
        change_text_canvas(
            canvas=self._main_canvas,
            text=f'added new participant {participant[required_field]!r}'
        )

        clean_participant_inputs(self, category=category, inputs=fields)
        remove_old_saves_if_exist(event_name=self._event_name)
        save_categories(self)
