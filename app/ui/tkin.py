from pathlib import Path

from settings.ui.const import (
    MAIN_CANVAS_KWARGS, NICKNAME_CANVAS_KWARGS, CREW_CANVAS_KWARGS,
    CITY_CANVAS_KWARGS, DEFAULT_DOWNLOAD_PATH, NICK_INPUT_COORDS,
    CITY_INPUT_COORDS, CREW_INPUT_COORDS,
)
from app.ui.widgets import (
    create_and_get_sex_radiobuttons, get_window,
    create_and_get_grid_size_radiobuttons, create_empty_strings,
    get_canvas, get_create_button, get_destination_button,
    get_curr_path_label, get_selected_sex, get_input
)


class BattleGridUI:
    def __init__(self) -> None:
        self._window = get_window()
        self._selected_sex = get_selected_sex(main_window=self._window)
        self._sex_radiobuttons = create_and_get_sex_radiobuttons(
            main_window=self._window, selected_sex=self._selected_sex
        )
        self._grid_size = create_and_get_grid_size_radiobuttons()
        create_empty_strings(main_window=self._window, rows=[5, 11])

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

        self._create_button = get_create_button(main_window=self._window)

        self._destination_path = str(Path(DEFAULT_DOWNLOAD_PATH).resolve())
        self._curr_path_label = get_curr_path_label(
            main_window=self._window, destination_path=self._destination_path
        )
        self._destination_button = get_destination_button(
            main_window=self._window, destination_path=self._destination_path,
            current_path_label=self._curr_path_label
        )

        self._window.mainloop()
