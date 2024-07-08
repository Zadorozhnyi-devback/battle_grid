from tkinter import Toplevel

from app.settings.ui.const import (
    CATEGORY_TITLE_INPUT_COORDS,
    CATEGORY_CANVAS_KWARGS,
    GRID_SIZE_CANVAS_KWARGS
)
from apps.ui.validators import validate_event_name_exists
from apps.ui.widgets.common import create_empty_strings
from apps.ui.widgets.events import (
    press_exit_cross_signal,
    top_level_closer,
    bind_esc_for_close
)
from apps.ui.widgets.inputs import get_input
from apps.ui.widgets.labels.creators import create_canvas
from apps.ui.widgets.radio import (
    create_grid_size_radio,
    create_category_type_radio
)

from .buttons import create_add_category_button


__all__ = (
    'create_add_category_toplevel',
)


def create_add_category_toplevel(self) -> None:
    if validate_event_name_exists(self) is True:
        add_category_toplevel = Toplevel(master=self._window)
        add_category_toplevel.focus_force()
        add_category_toplevel.resizable(False, False)

        self._category_input = get_input(
            frame=add_category_toplevel,
            **CATEGORY_TITLE_INPUT_COORDS
        )

        create_canvas(frame=add_category_toplevel, **CATEGORY_CANVAS_KWARGS)

        create_category_type_radio(
            frame=add_category_toplevel,
            selected_type=self._selected_category_type
        )
        create_add_category_button(self, frame=add_category_toplevel)

        add_category_toplevel.title(string='add category')
        setattr(self, '_add_category_toplevel', add_category_toplevel)

        bind_esc_for_close(self, frame_title='_add_category_toplevel')
        kwargs = {
            'self': self,
            'func': top_level_closer,
            'frame_title': '_add_category_toplevel'
        }
        press_exit_cross_signal(**kwargs)

        create_empty_strings(frame=add_category_toplevel, rows=[2, 4])

        create_grid_size_radio(
            self,
            window=add_category_toplevel,
            selected_size=self._selected_grid_size
        )
        create_canvas(frame=add_category_toplevel, **GRID_SIZE_CANVAS_KWARGS)

        add_category_toplevel.transient(master=self._window)
        add_category_toplevel.grab_set()
        self._window.wait_window(window=add_category_toplevel)
