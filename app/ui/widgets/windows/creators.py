import os
from tkinter.ttk import Style
from tkinter import Frame, PhotoImage, Tk, NORMAL, DISABLED, END
from typing import Dict, Union, List

from app.ui.const import BEGINNING
from app.ui.handlers.cleaners import clean_category_input
from app.ui.handlers.getters import (
    get_value_without_underscore,
    get_male_and_female_stats_text,
    get_category_info_text
)
from app.ui.handlers.updators import update_category_sex_stats_canvas
from app.ui.widgets.buttons.tab_control_creators import (
    create_open_edit_category_toplevel_button,
    create_unregister_participant_button,
    create_register_participant_button
)
from app.ui.widgets.common import create_empty_strings
from app.ui.widgets.events import (
    press_exit_cross_signal,
    main_window_closer,
    bind_esc_for_close
)
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels.creators import create_canvas
from app.ui.widgets.labels.getters import get_canvas
from app.ui.widgets.radio import get_sex_radio, get_default_radio
from app.ui.widgets.separators import create_separator
from app.ui.widgets.text import get_category_people_list
from settings.ui.const import (
    SELECTED_CATEGORY_TYPE_CANVAS_KWARGS,
    SELECTED_GRID_CANVAS_KWARGS,
    CATEGORY_INFO_FRAME_COORDS,
    REGISTRATION_FRAME_COORDS,
    DEFAULT_SEX,
    TEMP_INPUT_COORDS,
    NICK_INPUT_COORDS,
    CREW_INPUT_COORDS,
    CITY_INPUT_COORDS,
    NICK_CANVAS_KWARGS,
    CREW_CANVAS_KWARGS,
    CITY_CANVAS_KWARGS,
    TAB_LEFT_SEPARATOR_KWARGS,
    TAB_RIGHT_SEPARATOR_KWARGS,
    MALE_AND_FEMALE_CANVAS_KWARGS
)


def create_window(
    self,
    title: str,
    size: str,
    icon: str = None
) -> None:
    self._window = Tk()

    # binds
    bind_esc_for_close(self, frame_title='_window')
    kwargs = {
        'self': self,
        'func': main_window_closer,
        'frame_title': '_window'
    }
    press_exit_cross_signal(**kwargs)

    style = Style(master=self._window)
    style.theme_use(themename='aqua')

    if icon is not None:
        icon = f'{os.getcwd()}/static/{icon}'
        self._window.iconphoto(True, PhotoImage(file=icon))

    self._window.title(string=title)
    self._window.geometry(newGeometry=size)
    self._window.resizable(width=False, height=False)


def create_registration_frame(
    self,
    tab_frame: Frame,
    selected_category_type: str,
    category: str
) -> None:
    reg_frame = Frame(master=tab_frame)
    reg_frame.grid(**REGISTRATION_FRAME_COORDS)
    setattr(self, f'_{category}_registration_frame', reg_frame)

    create_empty_strings(frame=reg_frame, rows=[5])

    if selected_category_type == 'single':
        nick_canvas = get_canvas(frame=reg_frame, **NICK_CANVAS_KWARGS)
        setattr(self, f'_{category}_nick_canvas', nick_canvas)

        nick_input = get_input(frame=reg_frame, **NICK_INPUT_COORDS)
        setattr(self, f'_{category}_nick_input', nick_input)

        selected_sex = get_default_radio(window=reg_frame, value=DEFAULT_SEX)
        setattr(self, f'_{category}_selected_sex', selected_sex)

        sex_radio = get_sex_radio(frame=reg_frame, selected_sex=selected_sex)
        setattr(self, f'_{category}_sex_radio', sex_radio)

    create_canvas(frame=reg_frame, **CREW_CANVAS_KWARGS)
    create_canvas(frame=reg_frame, **CITY_CANVAS_KWARGS)

    crew_input = get_input(frame=reg_frame, **CREW_INPUT_COORDS)
    setattr(self, f'_{category}_crew_input', crew_input)

    city_input = get_input(frame=reg_frame, **CITY_INPUT_COORDS)
    setattr(self, f'_{category}_city_input', city_input)

    create_register_participant_button(self, window=reg_frame)
    create_unregister_participant_button(self, window=reg_frame)


def create_category_info_frame(self, tab_frame: Frame, category: str) -> None:
    info_frame = Frame(master=tab_frame)
    info_frame.grid(**CATEGORY_INFO_FRAME_COORDS)
    setattr(self, f'_{category}_info_frame', info_frame)

    grid_size = get_value_without_underscore(
        value=self._categories[category]['grid_size']
    )
    setattr(
        self,
        f'_{category}_selected_grid_canvas',
        get_canvas(
            frame=info_frame,
            text=f'grid: {grid_size}',
            **SELECTED_GRID_CANVAS_KWARGS
        )
    )

    setattr(
        self,
        f'_{category}_selected_category_type_canvas',
        get_canvas(
            frame=info_frame,
            text=f"type: {self._categories[category]['type']}",
            **SELECTED_CATEGORY_TYPE_CANVAS_KWARGS
        )
    )

    if self._categories[category]['type'] == 'single':
        setattr(
            self,
            f'_{category}_male_and_female_canvas',
            get_canvas(
                frame=info_frame,
                text=get_male_and_female_stats_text(),
                **MALE_AND_FEMALE_CANVAS_KWARGS
            )
        )
    else:
        create_empty_strings(frame=info_frame, rows=[2])

    create_open_edit_category_toplevel_button(self, window=info_frame)


def create_loaded_categories(
    self,
    json_data: Dict[str, Dict[str, Union[str, List[Dict[str, str]]]]]
) -> None:
    self._category_input = get_input(frame=self._window, **TEMP_INPUT_COORDS)
    for category, data in json_data.items():
        self._category_input.insert(BEGINNING, category)
        self._selected_category_type.set(data['type'])
        self._selected_grid_size.set(data['grid_size'])

        create_new_tab(self)

        self._categories[category]['participants'] = data['participants']

        participants = [p for p in data['text_widget'].split('\n') if p]

        if self._categories[category]['type'] == 'single':
            info_text = get_category_info_text(self, category=category)
            update_category_sex_stats_canvas(
                self,
                category=category,
                category_info_text=info_text
            )

        text_widget = self._categories[category]['text_widget']
        text_widget.configure(state=NORMAL)
        [text_widget.insert(END, f'{string}\n') for string in participants]
        text_widget.configure(state=DISABLED)

        clean_category_input(self)

    self._category_input.destroy()
    delattr(self, '_category_input')


def create_new_tab(self) -> None:
    category = self._category_input.get().lower()
    selected_category_type = self._selected_category_type.get()

    tab_frame = Frame(master=self._window)

    create_separator(frame=tab_frame, **TAB_LEFT_SEPARATOR_KWARGS)
    create_separator(frame=tab_frame, **TAB_RIGHT_SEPARATOR_KWARGS)

    participants = get_category_people_list(tab_frame=tab_frame)

    self._categories[category] = {
        'grid_size': self._selected_grid_size.get(),
        'type': selected_category_type,
        'participants': list(),
        'text_widget': participants
    }

    create_registration_frame(
        self,
        tab_frame=tab_frame,
        category=category,
        selected_category_type=selected_category_type
    )
    create_category_info_frame(self, tab_frame=tab_frame, category=category)

    self._tab_control.add(child=tab_frame, text=category)
    self._tab_control.select(tab_frame)

    clean_category_input(self)
