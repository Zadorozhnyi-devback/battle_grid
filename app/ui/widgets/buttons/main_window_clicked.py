import getpass
import json
from pathlib import Path
from tkinter import messagebox, Tk, Label, filedialog, TclError, Toplevel

from app.ui.const import BEGINNING
from app.ui.handlers.cleaners import (
    remove_old_categories,
    remove_old_saves_if_exist
)
from app.ui.handlers.savers import save_categories
from app.ui.handlers.updators import update_timestamp
from app.ui.validators import (
    validate_event_name_input,
    validate_event_name_exists
)
from app.ui.widgets.buttons.after_click_creators import (
    create_make_new_event_button,
    create_rename_event_button
)
from app.ui.widgets.buttons.toplevels.for_main_window.creators import (
    create_add_category_button
)
from app.ui.widgets.common import (
    get_selected_tab_title,
    create_empty_strings
)
from app.ui.widgets.events import (
    bind_esc_for_close,
    top_level_frame_closer,
    press_exit_cross_signal
)
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels.creators import create_canvas
from app.ui.widgets.labels.getters import get_canvas
from app.ui.widgets.labels.handlers import change_text_canvas
from app.ui.widgets.radio import (
    create_category_type_radio,
    create_grid_size_radio
)
from app.ui.widgets.windows.creators import create_loaded_categories
from settings.ui.const import (
    DEFAULT_DOWNLOAD_PATH,
    CURRENT_PATH,
    EVENT_NAME_TITLE_CANVAS_KWARGS,
    EVENT_NAME_INPUT_COORDS,
    CATEGORY_TITLE_INPUT_COORDS,
    CATEGORY_CANVAS_KWARGS,
    GRID_SIZE_CANVAS_KWARGS
)


def clicked_remove_category(self) -> None:
    selected_tab = self._tab_control.select()
    category = get_selected_tab_title(self)
    if category:
        answer = messagebox.askyesno(
            message=f"delete category {category!r}?"
        )
        if answer is True:
            self._tab_control.forget(selected_tab)
            self._categories.pop(category)

            update_timestamp(self, category=category)

            remove_old_saves_if_exist(event_name=self._event_name)
            save_categories(self)
    else:
        change_text_canvas(
            canvas=self._main_canvas,
            text='no categories to remove'
        )


def clicked_generate_grid(self) -> None:
    # TODO: here gonna init BattleGrid class instance
    tab_control = self._tab_control
    current_tab = tab_control.tab(tab_control.select(), 'text')


def clicked_choose_dir(
    main_window: Tk, curr_path_label: Label,
    destination_path: str = DEFAULT_DOWNLOAD_PATH
) -> None:
    directory = filedialog.askdirectory(
        # gonna work on mac, have to check for windows and linux
        # initialdir=os.path.normpath("C://") try on Windows
        parent=main_window,
        initialdir=f'/Users/{getpass.getuser()}/'
    )
    if directory is not None:
        destination_path = str(Path(directory).resolve())
    curr_path_label.configure(text=f'{CURRENT_PATH}: {destination_path}')


def clicked_save_event_name(self) -> None:
    if validate_event_name_input(self) is True:
        self._event_name = self._event_name_input.get()

        self._event_name_title = get_canvas(
            frame=self._window,
            text=self._event_name,
            **EVENT_NAME_TITLE_CANVAS_KWARGS,
        )
        self._event_name_input.destroy()
        self._save_event_name_button.destroy()

        create_make_new_event_button(self, frame=self._buttons_frame)
        create_rename_event_button(self, frame=self._buttons_frame)

        change_text_canvas(
            canvas=self._main_canvas,
            text=f"event {self._event_name!r} was created"
        )


def clicked_open_event(self) -> None:
    event_json = filedialog.askopenfilename(
        parent=self._window,
        initialdir=(
            f'/Users/{getpass.getuser()}/PycharmProjects/battle_grid/events/'
        )
    )
    if event_json:
        if hasattr(self, '_event_name_title'):
            try:
                self._event_name_title.destroy()
            except TclError:
                pass
            delattr(self, '_event_name_title')
        self._event_name_input.destroy()
        self._event_name_input = get_input(
            frame=self._window,
            **EVENT_NAME_INPUT_COORDS
        )
        self._event_name_input.insert(
            BEGINNING,
            event_json.split('/')[-1].split('_')[0]
        )

        clicked_save_event_name(self)
        change_text_canvas(
            canvas=self._main_canvas,
            text=f"event {self._event_name!r} was loaded"
        )

        with open(file=event_json, encoding='utf-8') as event_file:
            file_data = json.load(event_file)

        remove_old_categories(self)
        create_loaded_categories(self, json_data=file_data)


def clicked_open_add_category_toplevel(self) -> None:
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
            'func': top_level_frame_closer,
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
