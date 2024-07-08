from apps.ui.handlers.cleaners import (
    clean_participant_inputs,
    remove_old_saves_if_exist,
    clean_text_widget
)
from apps.ui.handlers.getters import (
    get_participant_fields,
    get_participant_string,
    get_category_info_text,
    get_category_type,
    get_required_field,
    get_participants,
    get_input_value,
)
from apps.ui.handlers.savers import save_categories
from apps.ui.handlers.updators import (
    add_new_participant_in_text_widget,
    update_category_sex_stats_canvas
)
from apps.ui.validators import validate_participant_exists
from apps.ui.widgets.labels.handlers import change_text_canvas
from apps.ui.widgets.tab_control.utils.common import get_selected_tab_title
from shared.utils import update_timestamp


__all__ = (
    'unregister_participant'
)


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

        update_timestamp(self, category=category)

        clean_participant_inputs(self, category=category, inputs=fields)
        remove_old_saves_if_exist(event_name=self._event_name)
        save_categories(self)
