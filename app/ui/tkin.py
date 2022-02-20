from pathlib import Path

from app.ui.widgets.buttons import (
    get_create_button, get_add_tab_button, get_destination_button,
    get_remove_tab_button
)
from app.ui.widgets.common import create_empty_strings
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels import get_canvas, get_curr_path_label
from app.ui.widgets.radio import (
    create_sex_radio, create_grid_size_radio,
    get_default_radio, create_category_type_radio
)
from app.ui.widgets.windows import get_window, get_tab_control
from settings.ui.const import (
    MAIN_CANVAS_KWARGS, NICKNAME_CANVAS_KWARGS, CREW_CANVAS_KWARGS,
    CITY_CANVAS_KWARGS, DEFAULT_DOWNLOAD_PATH, NICK_INPUT_COORDS,
    CITY_INPUT_COORDS, CREW_INPUT_COORDS, GRID_SIZE_CANVAS_KWARGS,
    NEW_CATEGORY_INPUT_COORDS,
)


class BattleGridUI:
    def __init__(self) -> None:
        self._window = get_window()

        self._selected_sex = get_default_radio(
            window=self._window, value='male'
        )
        create_sex_radio(
            main_window=self._window, selected_sex=self._selected_sex
        )

        self._grid_size_canvas = get_canvas(
            main_window=self._window, **GRID_SIZE_CANVAS_KWARGS
        )
        self._selected_grid_size = get_default_radio(
            window=self._window, value='8'
        )
        create_grid_size_radio(
            main_window=self._window, selected_size=self._selected_grid_size
        )

        self._categories = dict()
        self._selected_category_type = get_default_radio(
            window=self._window, value='single'
        )
        create_category_type_radio(
            window=self._window, selected_type=self._selected_category_type
        )

        create_empty_strings(main_window=self._window, rows=[5, 8, 10])

        self._main_canvas = get_canvas(
            main_window=self._window, **MAIN_CANVAS_KWARGS
        )
        self._nickname_canvas = get_canvas(
            main_window=self._window, **NICKNAME_CANVAS_KWARGS
        )
        self._city_canvas = get_canvas(
            main_window=self._window, **CITY_CANVAS_KWARGS
        )
        self._crew_canvas = get_canvas(
            main_window=self._window, **CREW_CANVAS_KWARGS
        )

        self._nick = get_input(main_window=self._window, **NICK_INPUT_COORDS)
        self._city = get_input(main_window=self._window, **CITY_INPUT_COORDS)
        self._crew = get_input(main_window=self._window, **CREW_INPUT_COORDS)
        self._category_input = get_input(
            main_window=self._window, **NEW_CATEGORY_INPUT_COORDS
        )

        self._create_button = get_create_button(cls=self)

        self._people = dict()
        self._tab_control = get_tab_control(main_window=self._window)
        self._add_tab_button = get_add_tab_button(cls=self)
        self._remove_tab_button = get_remove_tab_button(cls=self)

        self._destination_path = str(Path(DEFAULT_DOWNLOAD_PATH).resolve())
        self._curr_path_label = get_curr_path_label(
            main_window=self._window, destination_path=self._destination_path
        )
        self._destination_button = get_destination_button(
            main_window=self._window, destination_path=self._destination_path,
            current_path_label=self._curr_path_label
        )

        self._window.mainloop()
