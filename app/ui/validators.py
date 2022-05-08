from app.ui.handlers.getters import (
    get_participant_fields,
    get_required_field,
    get_amount_of_category_participants,
    get_grid_size,
    get_input_value
)
from app.ui.widgets.labels.getters import get_canvas
from app.ui.widgets.labels.handlers import change_text_canvas
from settings.ui.const import (
    EVENT_INPUT_CANVAS_KWARGS,
    EMPTY_EVENT_INPUT_CANVAS_TEXT,
    SAME_EVENT_NAME_CANVAS_TEXT,
    EVENT_NAME_IS_TOO_LONG_TEXT
)


def validate_empty_category_input(self, category: str) -> bool:
    if not category:
        change_text_canvas(
            canvas=self._main_canvas,
            text="category can't be empty"
        )
        return False
    return True


def validate_category_exists(self, category: str) -> bool:
    if self._categories.get(category, None):
        change_text_canvas(
            canvas=self._main_canvas,
            text=f'category {category!r} already exist'
        )
        return False
    return True


def validate_category_free_places(self, category: str, grid_size: str) -> bool:
    if grid_size.isdigit():
        amount = get_amount_of_category_participants(self, category)
        if amount > int(grid_size):
            change_text_canvas(
                canvas=self._main_canvas,
                text=f"Category is full (can't add more then {grid_size})"
            )
            return False


def validate_for_update_category(self, category: str) -> bool:
    if validate_empty_category_input(self, category) is False:
        return False

    grid_size = get_grid_size(self, category)
    if self._selected_grid_size.get() != grid_size:
        grid_size = self._selected_grid_size.get()
        if grid_size.isdigit():
            amount = get_amount_of_category_participants(self, category)
            if int(grid_size) < amount:
                change_text_canvas(
                    canvas=self._main_canvas,
                    text=f'Category already has {amount} participants'
                )
                return False

    if validate_category_free_places(self, category, grid_size) is False:
        return False

    return True


def validate_for_create_category(self) -> bool:
    category = self._category_input.get().lower()

    if validate_empty_category_input(self, category=category) is False:
        return False

    if validate_category_exists(self, category=category) is False:
        return False

    change_text_canvas(canvas=self._main_canvas, text='added new tab')
    return True


def validate_event_name_input(self) -> bool:
    event_name = self._event_name_input.get()
    if not event_name:
        change_text_canvas(
            canvas=self._main_canvas,
            text=EMPTY_EVENT_INPUT_CANVAS_TEXT
        )
        return False
    if len(event_name) > 16:
        change_text_canvas(
            canvas=self._main_canvas,
            text=EVENT_NAME_IS_TOO_LONG_TEXT
        )
        return False
    return True


def validate_new_event_name(self, new_event_name: str) -> bool:
    if hasattr(self, '_event_frame_canvas'):
        self._event_frame_canvas.destroy()
        delattr(self, '_event_frame_canvas')
    if not new_event_name:
        self._event_frame_canvas = get_canvas(
            frame=self._rename_window,
            text=EMPTY_EVENT_INPUT_CANVAS_TEXT,
            **EVENT_INPUT_CANVAS_KWARGS
        )
        return False
    if new_event_name == self._event_name:
        self._event_frame_canvas = get_canvas(
            frame=self._rename_window,
            text=SAME_EVENT_NAME_CANVAS_TEXT,
            **EVENT_INPUT_CANVAS_KWARGS
        )
        return False
    if len(new_event_name) > 16:
        self._event_frame_canvas = get_canvas(
            frame=self._rename_window,
            text=EVENT_NAME_IS_TOO_LONG_TEXT,
            **EVENT_INPUT_CANVAS_KWARGS
        )
        return False
    return True


def validate_event_name_exists(self) -> bool:
    if not hasattr(self, '_event_name'):
        change_text_canvas(
            canvas=self._main_canvas,
            text=EMPTY_EVENT_INPUT_CANVAS_TEXT
        )
        return False
    return True


def validate_participant_inputs(self, category: str, tab_type: str) -> bool:
    grid_size = get_grid_size(self, category=category)
    if validate_category_free_places(self, category, grid_size) is False:
        return False

    fields = get_participant_fields(tab_type=tab_type)
    max_length = 16 if grid_size in (8, 16) else 21
    for field in fields:
        if len(get_input_value(self, category, field)) > max_length:
            change_text_canvas(
                canvas=self._main_canvas,
                text=f'{field} input is too long'
            )
            return False

    required_field = get_required_field(self, category=category)
    field_value = get_input_value(self, category, required_field)

    if not field_value:
        change_text_canvas(
            canvas=self._main_canvas,
            text=f"{required_field!r} field can't be empty"
        )
        return False

    for participant in self._categories[category]['participants']:
        if participant[required_field] == field_value:
            change_text_canvas(
                canvas=self._main_canvas,
                text=f"{required_field} {field_value!r} already exist"
            )
            return False
    return True


def validate_participant_exists(
    self,
    category: str,
    required_field: str,
    value: str
) -> bool:
    if not any([
            participant[required_field]
            for participant in self._categories[category]['participants']
            if participant[required_field] == value
    ]):
        change_text_canvas(
            canvas=self._main_canvas,
            text=f"{required_field} {value!r} doesn't exist"
        )
        return False
    return True
