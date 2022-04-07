from typing import Dict

from app.ui.handlers.getters import get_participant_fields
from app.ui.widgets.labels.getters import get_canvas
from app.ui.widgets.labels.handlers import change_text_canvas
from settings.ui.const import (
    EMPTY_EVENT_INPUT_CANVAS_KWARGS,
    SAME_EVENT_NAME_CANVAS_KWARGS
)


def validate_empty_category_input(self, category: str) -> bool:
    if not category:
        change_text_canvas(
            canvas=self._main_canvas, text="category can't be empty"
        )
        return False
    return True


def validate_category_exists(self, category: str) -> bool:
    if category in self._categories.keys():
        change_text_canvas(canvas=self._main_canvas, text='category exist')
        return False
    return True


def validate_update_category(self) -> bool:
    category = self._category_input.get()
    if validate_empty_category_input(self=self, category=category) is False:
        return False
    return True


def validate_create_category(self) -> bool:
    category = self._category_input.get().lower()

    if validate_empty_category_input(self=self, category=category) is False:
        return False

    if validate_category_exists(self=self, category=category) is False:
        return False

    change_text_canvas(canvas=self._main_canvas, text='added new tab')
    return True


def validate_event_name_input(self) -> bool:
    event = self._event_name_input.get()
    if not event:
        change_text_canvas(
            canvas=self._main_canvas, text="event name can't be empty"
        )
        return False
    return True


def validate_new_event_name(self, new_event_name: str) -> bool:
    if hasattr(self, '_event_frame_canvas'):
        self._event_frame_canvas.destroy()
        delattr(self, '_event_frame_canvas')
    if not new_event_name:
        self._event_frame_canvas = get_canvas(
            frame=self._rename_window, **EMPTY_EVENT_INPUT_CANVAS_KWARGS
        )
        return False
    if new_event_name == self._event_name:
        self._event_frame_canvas = get_canvas(
            frame=self._rename_window, **SAME_EVENT_NAME_CANVAS_KWARGS
        )
        return False
    return True


def validate_event_name_exists(self) -> bool:
    if not hasattr(self, '_event_name'):
        change_text_canvas(
            canvas=self._main_canvas, text="event name can't be empty"
        )
        return False
    return True


def validate_participant_inputs(self, category: str, tab_type: str) -> bool:
    fields = get_participant_fields(tab_type=tab_type)
    max_length = 16 if self._selected_grid_size.get() in (8, 16) else 21
    for field in fields:
        if len(getattr(self, f'_{category}_{field}_input').get()) > max_length:
            change_text_canvas(
                canvas=self._main_canvas, text=f'{field} input is too long'
            )
            return False

    field = 'nick' if tab_type == 'single' else 'crew'
    field_value = (
        getattr(self, f'_{category}_{field}_input').get().capitalize()
    )
    for participant in self._categories[category]['participants']:
        if participant[field] == field_value:
            change_text_canvas(
                canvas=self._main_canvas,
                text=f"{field} {field_value!r} already exist"
            )
            return False
    return True


def validate_participant_required_field(
    self, tab_type: str, participant: Dict[str, str]
) -> bool:
    required_field = 'nick' if tab_type == 'single' else 'crew'
    if not participant[required_field]:
        change_text_canvas(
            canvas=self._main_canvas,
            text=f"{required_field!r} field can't be empty"
        )
        return False
    return True


def validate_participant_exists(
    self, category: str, field_to_remove: str, value: str
) -> bool:
    if not any([
            participant[field_to_remove]
            for participant in self._categories[category]['participants']
            if participant[field_to_remove] == value
    ]):
        change_text_canvas(
            canvas=self._main_canvas,
            text=f"{field_to_remove} {value!r} doesn't exist"
        )
        return False
    return True
