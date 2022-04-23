from pathlib import Path
from tkinter import Frame

from app.ui.widgets.buttons.main_window_creators import (
    create_open_add_category_toplevel_button,
    create_remove_category_button,
    create_destination_button,
    create_open_event_button
)
from app.ui.widgets.buttons.main_window_getters import (
    get_save_event_name_button
)
from app.ui.widgets.common import create_empty_strings
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels.creators import create_canvas
from app.ui.widgets.labels.getters import get_canvas, get_curr_path_label
from app.ui.widgets.radio import get_default_radio
from app.ui.widgets.windows.creators import create_window
from app.ui.widgets.windows.getters import get_tab_control
from settings.ui.buttons import EVENT_FRAME_BUTTONS_COORDS
from settings.ui.const import (
    MAIN_CANVAS_KWARGS, DEFAULT_DOWNLOAD_PATH,
    DEFAULT_GRID_SIZE, DEFAULT_CATEGORY_TYPE, EVENT_NAME_INPUT_COORDS,
    EVENT_NAME_CANVAS_KWARGS, MAIN_WINDOW_TITLE, MAIN_WINDOW_SIZE
)


class BattleGridUI:
    def __init__(self) -> None:
        create_window(
            self, title=MAIN_WINDOW_TITLE,
            size=MAIN_WINDOW_SIZE, icon='jordan.png'
        )
        self._main_canvas = get_canvas(
            frame=self._window, **MAIN_CANVAS_KWARGS  # noqa
        )

        self._destination_path = str(Path(DEFAULT_DOWNLOAD_PATH).resolve())
        self._curr_path_label = get_curr_path_label(
            main_window=self._window,  # noqa
            destination_path=self._destination_path
        )
        create_destination_button(
            main_window=self._window,  # noqa
            destination_path=self._destination_path,
            current_path_label=self._curr_path_label
        )

        create_canvas(frame=self._window, **EVENT_NAME_CANVAS_KWARGS)  # noqa
        self._event_name_input = get_input(
            frame=self._window, **EVENT_NAME_INPUT_COORDS  # noqa
        )

        self._buttons_frame = Frame(master=self._window)  # noqa
        self._buttons_frame.grid(**EVENT_FRAME_BUTTONS_COORDS)

        self._save_event_name_button = get_save_event_name_button(
            self, frame=self._buttons_frame
        )
        create_open_event_button(self, frame=self._buttons_frame)

        self._selected_grid_size = get_default_radio(
            window=self._window, value=DEFAULT_GRID_SIZE  # noqa
        )

        self._categories = dict()
        self._selected_category_type = get_default_radio(
            window=self._window, value=DEFAULT_CATEGORY_TYPE  # noqa
        )

        create_empty_strings(frame=self._window, rows=[3, 6, 8, 10])  # noqa

        create_open_add_category_toplevel_button(self)
        create_remove_category_button(self)

        self._tab_control = get_tab_control(main_window=self._window)  # noqa

        self._window.focus_force()  # noqa
        self._window.mainloop()  # noqa
