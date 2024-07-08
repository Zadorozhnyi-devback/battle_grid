from apps.ui.handlers.cleaners import (
    clean_participant_inputs,
    remove_old_saves_if_exist
)
from apps.ui.handlers.getters import (
    get_participant_fields,
    get_participant_info,
    get_participant_string,
    get_category_info_text,
    get_category_type,
    get_required_field,
    get_amount_of_category_participants
)
from apps.ui.handlers.savers import save_categories
from apps.ui.handlers.updators import (
    add_new_participant_in_text_widget,
    update_category_sex_stats_canvas
)
from apps.ui.validators import validate_participant_inputs
from apps.ui.widgets.labels.handlers import change_text_canvas
from apps.ui.widgets.tab_control.utils.common import get_selected_tab_title
from shared.utils import update_timestamp


__all__ = (
    'register_new_participant',
)


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

        update_timestamp(self, category=category)

        clean_participant_inputs(self, category=category, inputs=fields)
        remove_old_saves_if_exist(event_name=self._event_name)
        save_categories(self)
