from typing import Dict

from app.ui.handlers import get_participant_fields
from app.ui.widgets.labels import change_text_canvas


def validate_category_existing(cls) -> bool:
    if not cls._category_input.get() in cls._categories.keys():
        change_text_canvas(canvas=cls._main_canvas, text='added new tab')
        return True
    else:
        change_text_canvas(canvas=cls._main_canvas, text='category exist')
        return False


def validate_input(cls, current_tab: str, tab_type: str) -> bool:
    entries = get_participant_fields(tab_type=tab_type)
    max_length = 16 if cls._selected_grid_size.get() in (8, 16) else 21
    for entry in entries:
        if len(getattr(cls, f'_{entry}').get()) > max_length:
            change_text_canvas(
                canvas=cls._main_canvas, text=f'{entry} input is too long'
            )
            return False

    field = 'nick' if tab_type == 'single' else 'crew'
    field_value = getattr(cls, f'_{field}').get()
    for participant in cls._categories[current_tab]['participants']:
        if participant[field] == field_value:
            change_text_canvas(
                canvas=cls._main_canvas,
                text=f"{field} '{field_value}' already exist"
            )
            return False
    return True


def validate_required_field(
    cls, tab_type: str, participant: Dict[str, str]
) -> bool:
    required_field = 'nick' if tab_type == 'single' else 'crew'
    # if required_field in participant.keys():
    if not participant[required_field]:
        change_text_canvas(
            canvas=cls._main_canvas,
            text=f"'{required_field}' field can't be empty"
        )
        return False
    return True


def validate_participant_exists(
    cls, current_tab: str, field_to_remove: str, value: str
) -> bool:
    if not any([
            participant[field_to_remove]
            for participant in cls._categories[current_tab]['participants']
            if participant[field_to_remove] == value
    ]):
        change_text_canvas(
            canvas=cls._main_canvas,
            text=f"{field_to_remove} '{value}' doesn't exist"
        )
        return False
    return True
