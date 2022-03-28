from pathlib import Path
from tkinter import Frame

from app.ui.widgets.buttons.main_window_creators import (
    create_add_tab_button, create_remove_tab_button, create_destination_button,
    get_save_event_name_button, create_open_event_button
)
from app.ui.widgets.common import create_empty_strings
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels import get_canvas, get_curr_path_label
from app.ui.widgets.radio import (
    create_grid_size_radio, get_default_radio, create_category_type_radio
)
from app.ui.widgets.windows import get_window, get_tab_control
from settings.ui.buttons import EVENT_FRAME_BUTTONS_COORDS
from settings.ui.const import (
    MAIN_CANVAS_KWARGS, DEFAULT_DOWNLOAD_PATH, GRID_SIZE_CANVAS_KWARGS,
    DEFAULT_GRID_SIZE, NEW_CATEGORY_INPUT_COORDS, NEW_CATEGORY_CANVAS_KWARGS,
    DEFAULT_CATEGORY_TYPE, EVENT_NAME_INPUT_COORDS, EVENT_NAME_CANVAS_KWARGS,
    MAIN_WINDOW_TITLE, MAIN_WINDOW_SIZE, GRID_SIZE_RADIO_FRAME_COORDS
)


class BattleGridUI:
    def __init__(self) -> None:
        self._window = get_window(
            cls=self, title=MAIN_WINDOW_TITLE,
            size=MAIN_WINDOW_SIZE, icon='jordan.png'
        )
        self._main_canvas = get_canvas(
            window=self._window, **MAIN_CANVAS_KWARGS
        )

        self._destination_path = str(Path(DEFAULT_DOWNLOAD_PATH).resolve())
        self._curr_path_label = get_curr_path_label(
            main_window=self._window, destination_path=self._destination_path
        )
        create_destination_button(
            main_window=self._window, destination_path=self._destination_path,
            current_path_label=self._curr_path_label
        )

        self._event_name_canvas = get_canvas(
            window=self._window, **EVENT_NAME_CANVAS_KWARGS
        )
        self._event_name_input = get_input(
            window=self._window, **EVENT_NAME_INPUT_COORDS
        )

        self._buttons_frame = Frame(master=self._window)
        self._buttons_frame.grid(**EVENT_FRAME_BUTTONS_COORDS)

        self._save_event_name_button = get_save_event_name_button(
            cls=self, frame=self._buttons_frame
        )
        create_open_event_button(
            cls=self, frame=self._buttons_frame
        )

        self._grid_size_canvas = get_canvas(
            window=self._window, **GRID_SIZE_CANVAS_KWARGS
        )
        self._selected_grid_size = get_default_radio(
            window=self._window, value=DEFAULT_GRID_SIZE
        )
        create_grid_size_radio(
            window=self._window, selected_size=self._selected_grid_size,
            coords=GRID_SIZE_RADIO_FRAME_COORDS
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

        create_add_tab_button(cls=self)
        create_remove_tab_button(cls=self)

        self._people = dict()
        self._tab_control = get_tab_control(main_window=self._window)

        self._window.focus_force()
        self._window.mainloop()
