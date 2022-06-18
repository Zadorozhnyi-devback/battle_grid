from apps.ui.widgets.labels.getters import get_canvas
from apps.ui.widgets.menu import create_menu_bar
from apps.ui.widgets.menu.file.event.create import create_event_toplevel
from apps.ui.widgets.radio import get_default_radio
from apps.ui.widgets.windows.creators import create_window
from app.settings.ui.const import (
    MAIN_CANVAS_KWARGS,
    DEFAULT_GRID_SIZE,
    DEFAULT_CATEGORY_TYPE,
    MAIN_WINDOW_TITLE,
    MAIN_WINDOW_SIZE
)


__all__ = (
    'BattleGridUI',
)


class BattleGridUI:
    def __init__(self) -> None:
        create_window(
            self,
            title=MAIN_WINDOW_TITLE,
            size=MAIN_WINDOW_SIZE,
            icon='jordan.png'
        )
        create_menu_bar(self)

        self._categories = dict()

        self._main_canvas = get_canvas(
            frame=self._window,  # noqa
            **MAIN_CANVAS_KWARGS
        )

        self._selected_grid_size = get_default_radio(
            window=self._window,  # noqa
            value=DEFAULT_GRID_SIZE
        )

        self._selected_category_type = get_default_radio(
            window=self._window,  # noqa
            value=DEFAULT_CATEGORY_TYPE
        )

        create_event_toplevel(self)

        self._window.focus_force()  # noqa
        self._window.mainloop()  # noqa
