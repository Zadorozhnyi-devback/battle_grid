from tkinter import Toplevel

from app.settings.ui.const import (
    CATEGORY_TITLE_INPUT_COORDS,
    CATEGORY_CANVAS_KWARGS,
    GRID_SIZE_CANVAS_KWARGS
)
from apps.ui.const import BEGINNING
from apps.ui.handlers.getters import get_category_type, get_grid_size
from apps.ui.validators import validate_event_name_exists
from .buttons import create_save_categories_button
from apps.ui.widgets.common import create_empty_strings
from apps.ui.widgets.events import (
    bind_esc_for_close,
    top_level_closer,
    press_exit_cross_signal
)
from apps.ui.widgets.inputs import get_input
from apps.ui.widgets.labels.creators import create_canvas
from apps.ui.widgets.radio import (
    create_category_type_radio,
    create_grid_size_radio
)
from apps.ui.widgets.tab_control.utils.common import get_selected_tab_title


__all__ = (
    'create_edit_category_toplevel',
)


def create_edit_category_toplevel(self) -> None:
    if validate_event_name_exists(self) is True:
        category_frame_window = Toplevel(master=self._window)
        category_frame_window.focus_force()
        category_frame_window.resizable(False, False)

        self._category_input = get_input(
            frame=category_frame_window,
            **CATEGORY_TITLE_INPUT_COORDS
        )

        create_canvas(frame=category_frame_window, **CATEGORY_CANVAS_KWARGS)

        category = get_selected_tab_title(self)
        category_frame = f'_{category}_toplevel_frame'

        self._category_input.insert(BEGINNING, category)
        self._selected_category_type.set(get_category_type(self, category))
        self._selected_grid_size.set(get_grid_size(self, category))

        if not self._categories[category]['participants']:
            create_category_type_radio(
                frame=category_frame_window,
                selected_type=self._selected_category_type
            )

        create_empty_strings(frame=category_frame_window, rows=[2, 4])

        create_grid_size_radio(
            self,
            window=category_frame_window,
            selected_size=self._selected_grid_size,
            category=category
        )
        create_canvas(frame=category_frame_window, **GRID_SIZE_CANVAS_KWARGS)

        create_save_categories_button(
            self,
            frame=category_frame_window,
            category=category
        )

        category_frame_window.title(string='edit category')
        setattr(self, category_frame, category_frame_window)

        bind_esc_for_close(self, frame_title=category_frame)
        kwargs = {
            'self': self,
            'func': top_level_closer,
            'frame_title': category_frame
        }
        press_exit_cross_signal(**kwargs)

        category_frame_window.transient(master=self._window)
        category_frame_window.grab_set()
        self._window.wait_window(window=category_frame_window)
