import os
from tkinter import (
    Tk, PhotoImage, Frame, Scrollbar, Text, NONE, DISABLED
)
from tkinter.ttk import Style, Notebook, Separator
from typing import Tuple

from app.ui.handlers import clean_category_input
from app.ui.widgets.buttons.tab_control_creators import (
    create_register_participant_button, create_unregister_participant_button,
    create_change_category_grid_size_button
)
from app.ui.widgets.common import create_empty_strings
from app.ui.widgets.events import bind_esc_for_close, main_window_closer
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels import get_canvas
from app.ui.widgets.radio import get_default_radio, create_sex_radio
from settings.ui.const import (
    TAB_CONTROL_WINDOW_SIZE, NICK_CANVAS_KWARGS,
    CITY_CANVAS_KWARGS, CREW_CANVAS_KWARGS, NICK_INPUT_COORDS,
    CITY_INPUT_COORDS, CREW_INPUT_COORDS, DEFAULT_SEX,
    TAB_LEFT_SEPARATOR_KWARGS, TAB_RIGHT_SEPARATOR_KWARGS,
    SELECTED_GRID_CANVAS_KWARGS, CATEGORY_INFO_FRAME_COORDS,
    TAB_CONTROL_WINDOW_COORDS, CREATE_REGISTRATION_FRAME_COORDS
)


def get_category_people_list(window: Frame) -> Text:

    scrollbar = Scrollbar(master=window)
    scrollbar.grid(column=6, row=0, rowspan=100, pady=(4, 4), sticky='ens')

    text = Text(
        master=window,
        width=40, heigh=18.5,
        yscrollcommand=scrollbar.set, wrap=NONE,
        font=('Helvetica', 13), state=DISABLED
    )
    text.grid(column=5, row=0, rowspan=100, sticky='E', pady=(4, 4))

    scrollbar.config(command=text.yview)
    window.columnconfigure(2, weight=1)
    return text


def create_separator(
    frame: Frame, orient: str, column: int, row: int,
    row_span: int, sticky: str, pad_y: Tuple[int], pad_x: Tuple[int]
) -> None:
    separator = Separator(master=frame, orient=orient)
    separator.grid(
        column=column, row=row, rowspan=row_span,
        sticky=sticky, pady=pad_y, padx=pad_x
    )


def create_registration_frame(
    cls, tab_frame: Frame, selected_category_type: str, category: str
) -> None:
    registration_frame = Frame(master=tab_frame)
    registration_frame.grid(**CREATE_REGISTRATION_FRAME_COORDS)

    create_empty_strings(window=registration_frame, rows=[5])

    if selected_category_type == 'single':
        cls._nick_canvas = get_canvas(
            window=registration_frame, **NICK_CANVAS_KWARGS
        )

        nick_input = get_input(window=registration_frame, **NICK_INPUT_COORDS)
        setattr(cls, f'_{category}_nick_input', nick_input)

        selected_sex = get_default_radio(
            window=registration_frame, value=DEFAULT_SEX
        )
        setattr(cls, f'_{category}_selected_sex', selected_sex)
        create_sex_radio(
            main_window=registration_frame, selected_sex=selected_sex
        )

    cls._crew_canvas = get_canvas(
        window=registration_frame, **CREW_CANVAS_KWARGS
    )
    cls._city_canvas = get_canvas(
        window=registration_frame, **CITY_CANVAS_KWARGS
    )

    crew_input = get_input(window=registration_frame, **CREW_INPUT_COORDS)
    setattr(cls, f'_{category}_crew_input', crew_input)

    city_input = get_input(window=registration_frame, **CITY_INPUT_COORDS)
    setattr(cls, f'_{category}_city_input', city_input)

    create_register_participant_button(cls=cls, window=registration_frame)
    create_unregister_participant_button(cls=cls, window=registration_frame)


def create_category_info_frame(cls, tab_frame: Frame, category: str) -> None:
    frame = Frame(master=tab_frame)
    frame.grid(**CATEGORY_INFO_FRAME_COORDS)

    grid_size = ' '.join(cls._categories[category]['grid_size'].split('_'))
    setattr(
        cls,
        f'_{category}_selected_grid_canvas',
        get_canvas(
            window=frame, text=f"grid: {grid_size}",
            **SELECTED_GRID_CANVAS_KWARGS
        )
    )

    create_change_category_grid_size_button(
        cls=cls, window=frame, category=category)


def create_new_tab(cls) -> None:
    category = cls._category_input.get()
    print('category', category)
    selected_category_type = cls._selected_category_type.get()

    frame = Frame(master=cls._window)

    create_separator(frame=frame, **TAB_LEFT_SEPARATOR_KWARGS)
    create_separator(frame=frame, **TAB_RIGHT_SEPARATOR_KWARGS)

    participants = get_category_people_list(window=frame)

    cls._categories[category] = {
        'grid_size': cls._selected_grid_size.get(),
        'type': selected_category_type,  # crew or single
        'participants': list(),
        'text_widget': participants
    }

    create_registration_frame(
        cls=cls, tab_frame=frame, category=category,
        selected_category_type=selected_category_type
    )
    create_category_info_frame(cls=cls, tab_frame=frame, category=category)

    cls._tab_control.add(child=frame, text=category)
    cls._tab_control.select(frame)

    clean_category_input(cls=cls)


def get_tab_control(main_window: Tk) -> Notebook:
    tab_control = Notebook(master=main_window, **TAB_CONTROL_WINDOW_SIZE)
    tab_control.enable_traversal()
    tab_control.grid(**TAB_CONTROL_WINDOW_COORDS)
    return tab_control


def get_window(cls, title: str, size: str, icon: str = None) -> Tk:
    window = Tk()

    # binds
    bind_esc_for_close(cls=cls, frame=window, window_title='_window')
    window.protocol(
        'WM_DELETE_WINDOW', lambda: main_window_closer(cls=cls, frame=window)
    )

    style = Style(master=window)
    style.theme_use(themename='aqua')

    if icon is not None:
        icon = f'{os.getcwd()}/static/{icon}'
        window.iconphoto(True, PhotoImage(file=icon))

    window.title(string=title)
    window.geometry(newGeometry=size)
    window.resizable(False, False)
    return window
