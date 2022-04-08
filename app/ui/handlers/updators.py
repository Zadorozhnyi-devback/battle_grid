from app.ui.handlers.getters import get_value_without_underscore
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels.getters import get_canvas
from app.ui.widgets.labels.handlers import change_text_canvas
from app.ui.widgets.radio import (get_sex_radio,
                                  get_default_radio)
from settings.ui.const import (NICK_CANVAS_KWARGS,
                               NICK_INPUT_COORDS,
                               DEFAULT_SEX)


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


def update_category_data(self, category: str) -> None:
    category_type = self._selected_category_type.get()
    if category_type != self._categories[category]['type']:
        self._categories[category]['type'] = category_type
        category_type_canvas = getattr(
            self, f'_{category}_selected_category_type_canvas'
        )
        change_text_canvas(
            canvas=category_type_canvas, text=f'type: {category_type}'
        )

        build_widgets_by_category_type(
            self=self, category_type=category_type, category=category
        )

    grid_size = self._selected_grid_size.get()
    if self._categories[category]['grid_size'] != grid_size:
        self._categories[category]['grid_size'] = grid_size
        grid_size_canvas = getattr(self, f'_{category}_selected_grid_canvas')

        clean_grid_size = get_value_without_underscore(value=grid_size)
        change_text_canvas(
            canvas=grid_size_canvas, text=f"grid: {clean_grid_size}"
        )

    new_title = self._category_input.get()
    if category != new_title:
        self._categories[new_title] = self._categories[category]
        self._tab_control.tab(self._tab_control.select(), text=new_title)
        rename_class_attributes(
            self=self, new_title=new_title, old_title=category
        )
        self._categories.pop(category)
