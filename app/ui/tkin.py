from pathlib import Path

from app.ui.widgets.buttons.main_window_getters import (
    get_add_tab_button, get_remove_tab_button, get_destination_button
)
from app.ui.widgets.common import create_empty_strings
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels import get_canvas, get_curr_path_label
from app.ui.widgets.radio import (
    create_grid_size_radio, get_default_radio, create_category_type_radio
)
from app.ui.widgets.windows import get_window, get_tab_control
from settings.ui.const import (
    MAIN_CANVAS_KWARGS,
    DEFAULT_DOWNLOAD_PATH,
    GRID_SIZE_CANVAS_KWARGS,
    NEW_CATEGORY_INPUT_COORDS, DEFAULT_GRID_SIZE, DEFAULT_CATEGORY_TYPE,
    NEW_CATEGORY_CANVAS_KWARGS,
)


class BattleGridUI:
    def __init__(self) -> None:
        self._window = get_window()
        self._main_canvas = get_canvas(
            window=self._window, **MAIN_CANVAS_KWARGS
        )

        self._destination_path = str(Path(DEFAULT_DOWNLOAD_PATH).resolve())
        self._curr_path_label = get_curr_path_label(
            main_window=self._window, destination_path=self._destination_path
        )
        self._destination_button = get_destination_button(
            main_window=self._window, destination_path=self._destination_path,
            current_path_label=self._curr_path_label
        )

        self._grid_size_canvas = get_canvas(
            window=self._window, **GRID_SIZE_CANVAS_KWARGS
        )
        self._selected_grid_size = get_default_radio(
            window=self._window, value=DEFAULT_GRID_SIZE
        )
        create_grid_size_radio(
            main_window=self._window, selected_size=self._selected_grid_size
        )

        self._new_category_canvas = get_canvas(
            window=self._window, **NEW_CATEGORY_CANVAS_KWARGS
        )
        self._category_input = get_input(
            window=self._window, **NEW_CATEGORY_INPUT_COORDS
        )

        self._categories = dict()
        self._selected_category_type = get_default_radio(
            window=self._window, value=DEFAULT_CATEGORY_TYPE
        )
        create_category_type_radio(
            window=self._window, selected_type=self._selected_category_type
        )

        create_empty_strings(window=self._window, rows=[3, 6])

        self._add_tab_button = get_add_tab_button(cls=self)
        self._remove_tab_button = get_remove_tab_button(cls=self)

        self._people = dict()
        self._tab_control = get_tab_control(main_window=self._window)

        self._window.mainloop()
