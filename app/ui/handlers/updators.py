from tkinter import NORMAL, DISABLED, END

from app.ui.handlers.cleaners import remove_old_saves_if_exist
from app.ui.handlers.getters import (
    get_value_without_underscore,
    get_grid_size,
    get_text_widget,
    get_category_type
)
from app.ui.handlers.savers import save_categories
from app.ui.handlers.setters import set_grid_size, set_category_type
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels.getters import get_canvas
from app.ui.widgets.labels.handlers import change_text_canvas
from app.ui.widgets.radio import (
    get_sex_radio,
    get_default_radio
)
from settings.ui.const import (
    NICK_CANVAS_KWARGS,
    NICK_INPUT_COORDS,
    DEFAULT_SEX
)
from shared.utils import get_current_datetime


def rename_class_attributes(self, new_title: str, old_title: str) -> None:
    attributes = ['_info_frame',
                  '_selected_category_type_canvas',
                  '_selected_grid_canvas',
                  '_registration_frame',
                  '_crew_input',
                  '_city_input']

    if self._selected_category_type.get() == 'single':
        additional_attributes = ['_nick_canvas',
                                 '_nick_input',
                                 '_selected_sex',
                                 '_sex_radio']
        attributes = [*attributes, *additional_attributes]

    for attr in attributes:
        widget = getattr(self, f'_{old_title}{attr}')
        delattr(self, f'_{old_title}{attr}')
        setattr(self, f'_{new_title}{attr}', widget)


def build_widgets_by_category_type(
    self, category_type: str, category: str
) -> None:
    if category_type == 'crew' and hasattr(self, f'_{category}_nick_canvas'):
        for attribute in ('_nick_canvas', '_nick_input', '_sex_radio'):
            getattr(self, f'_{category}{attribute}').destroy()
            delattr(self, f'_{category}{attribute}')
        delattr(self, f'_{category}_selected_sex')

    elif (
        category_type == 'single'
        and not hasattr(self, f'_{category}_nick_canvas')
    ):
        reg_frame = getattr(self, f'_{category}_registration_frame')

        nick_canvas = get_canvas(frame=reg_frame, **NICK_CANVAS_KWARGS)
        setattr(self, f'_{category}_nick_canvas', nick_canvas)

        nick_input = get_input(frame=reg_frame, **NICK_INPUT_COORDS)
        setattr(self, f'_{category}_nick_input', nick_input)

        selected_sex = get_default_radio(window=reg_frame, value=DEFAULT_SEX)
        setattr(self, f'_{category}_selected_sex', selected_sex)
        sex_radio = get_sex_radio(frame=reg_frame, selected_sex=selected_sex)
        setattr(self, f'_{category}_sex_radio', sex_radio)


def update_timestamp(self, category: str) -> None:
    self._categories[category]['updated_at'] = get_current_datetime()


def update_category_data(self, category: str) -> None:
    category_type = self._selected_category_type.get()
    if category_type != get_category_type(self, category):
        set_category_type(self, category, category_type)
        category_type_canvas = getattr(
            self, f'_{category}_selected_category_type_canvas'
        )
        change_text_canvas(
            canvas=category_type_canvas, text=f'type: {category_type}'
        )

        build_widgets_by_category_type(
            self, category_type=category_type, category=category
        )

    selected_grid_size = self._selected_grid_size.get()
    if get_grid_size(self, category) != selected_grid_size:
        set_grid_size(self, category, selected_grid_size)
        grid_size_canvas = getattr(self, f'_{category}_selected_grid_canvas')

        clean_grid_size = get_value_without_underscore(
            value=selected_grid_size
        )
        change_text_canvas(
            canvas=grid_size_canvas, text=f"grid: {clean_grid_size}"
        )

    new_title = self._category_input.get()
    if category != new_title:
        self._categories[new_title] = self._categories[category]
        self._tab_control.tab(self._tab_control.select(), text=new_title)
        rename_class_attributes(
            self, new_title=new_title, old_title=category
        )
        self._categories.pop(category)

    update_timestamp(self, category=new_title)

    remove_old_saves_if_exist(event_name=self._event_name)
    save_categories(self)


def update_category_sex_stats_canvas(
    self,
    category_info_text: str,
    category: str
) -> None:
    category_info_canvas = getattr(self, f'_{category}_male_and_female_canvas')

    change_text_canvas(canvas=category_info_canvas, text=category_info_text)


def add_new_participant_in_text_widget(
    self,
    participant_string: str,
    category: str,
    index: int
) -> None:
    text_widget = get_text_widget(self, category)
    text_widget.configure(state=NORMAL)
    text_widget.insert(END, f'{index}. {participant_string}\n')
    text_widget.configure(state=DISABLED)
