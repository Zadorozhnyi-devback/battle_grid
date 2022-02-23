import os
from tkinter import Tk, PhotoImage, Frame, Grid
from tkinter.ttk import Style, Notebook

from app.ui.widgets.buttons.tab_control_getters import get_registration_button
from app.ui.widgets.common import create_empty_strings
from app.ui.widgets.events import closer
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels import get_canvas
from app.ui.widgets.radio import get_default_radio, create_sex_radio
from settings.ui.const import (
    WINDOW_TITLE, WINDOW_SIZE, TAB_CONTROL_WINDOW_SIZE, NICKNAME_CANVAS_KWARGS,
    CITY_CANVAS_KWARGS, CREW_CANVAS_KWARGS, NICK_INPUT_COORDS,
    CITY_INPUT_COORDS, CREW_INPUT_COORDS, DEFAULT_SEX
)


def create_new_tab(cls) -> None:
    category = cls._category_input.get()
    selected_category_type = cls._selected_category_type.get()
    frame = Frame(master=cls._window)
    cls._categories[category] = {
        'grid_size': cls._selected_grid_size.get(),
        'type': selected_category_type,  # crew or single
        'participants': list()
    }

    create_empty_strings(window=frame, rows=[4])

    cls._city_canvas = get_canvas(window=frame, **CITY_CANVAS_KWARGS)
    cls._crew_canvas = get_canvas(window=frame, **CREW_CANVAS_KWARGS)

    if selected_category_type == 'single':
        cls._nick_canvas = get_canvas(window=frame, **NICKNAME_CANVAS_KWARGS)
        cls._nick = get_input(window=frame, **NICK_INPUT_COORDS)
        cls._selected_sex = get_default_radio(window=frame, value=DEFAULT_SEX)
        create_sex_radio(main_window=frame, selected_sex=cls._selected_sex)

    cls._crew = get_input(window=frame, **CREW_INPUT_COORDS)
    cls._city = get_input(window=frame, **CITY_INPUT_COORDS)

    cls._create_button = get_registration_button(cls=cls, window=frame)
    cls._tab_control.add(frame, text=category)


def get_tab_control(main_window: Tk) -> Notebook:
    tab_control = Notebook(master=main_window, **TAB_CONTROL_WINDOW_SIZE)
    tab_control.enable_traversal()
    tab_control.grid(column=0, row=14, columnspan=40, sticky='W')
    return tab_control


def get_window() -> Tk:
    window = Tk()

    # binds
    window.bind(
        '<Escape>',
        lambda event, w=window: closer(event, main_window=w)
    )

    style = Style(master=window)
    style.theme_use('aqua')
    icon = f'{os.getcwd()}/static/jordan.png'
    window.iconphoto(True, PhotoImage(file=icon))
    window.title(WINDOW_TITLE)
    window.geometry(WINDOW_SIZE)
    window.resizable(False, False)
    return window
