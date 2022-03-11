import os
from tkinter import (
    Tk, PhotoImage, Frame, Scrollbar, Text, NONE, VERTICAL, DISABLED
)
from tkinter.ttk import Style, Notebook, Separator

from app.ui.handlers import clean_category_input
from app.ui.widgets.buttons.tab_control_getters import (
    get_register_button, get_unregister_button
)
from app.ui.widgets.common import create_empty_strings
from app.ui.widgets.events import closer
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels import get_canvas
from app.ui.widgets.radio import get_default_radio, create_sex_radio
from settings.ui.const import (
    WINDOW_TITLE, WINDOW_SIZE, TAB_CONTROL_WINDOW_SIZE, NICK_CANVAS_KWARGS,
    CITY_CANVAS_KWARGS, CREW_CANVAS_KWARGS, NICK_INPUT_COORDS,
    CITY_INPUT_COORDS, CREW_INPUT_COORDS, DEFAULT_SEX
)


def get_category_people_list(window: Frame) -> Text:
    separator = Separator(master=window, orient=VERTICAL)
    separator.grid(
        column=2, row=0, rowspan=100, sticky='ens', pady=(6, 6), padx=(0, 4)
    )

    scrollbar = Scrollbar(master=window)
    scrollbar.grid(column=4, row=0, rowspan=100, pady=(4, 4), sticky='ns')

    text = Text(
        master=window,
        width=50, heigh=18.5,
        yscrollcommand=scrollbar.set, wrap=NONE,
        font=('Helvetica', 13), state=DISABLED
    )
    text.grid(column=3, row=0, rowspan=100, sticky='W', pady=(4, 4))

    scrollbar.config(command=text.yview)
    window.columnconfigure(2, weight=1)
    return text


def create_new_tab(cls) -> None:
    category = cls._category_input.get()
    print('category', category)
    selected_category_type = cls._selected_category_type.get()
    frame = Frame(master=cls._window)

    participants = get_category_people_list(window=frame)
    cls._categories[category] = {
        'grid_size': cls._selected_grid_size.get(),
        'type': selected_category_type,  # crew or single
        'participants': list(),
        'text_widget': participants
    }

    create_empty_strings(window=frame, rows=[4])

    if selected_category_type == 'single':
        cls._nick_canvas = get_canvas(window=frame, **NICK_CANVAS_KWARGS)

        nick_input = get_input(window=frame, **NICK_INPUT_COORDS)
        setattr(cls, f'_{category}_nick_input', nick_input)

        selected_sex = get_default_radio(window=frame, value=DEFAULT_SEX)
        setattr(cls, f'_{category}_selected_sex', selected_sex)
        create_sex_radio(main_window=frame, selected_sex=selected_sex)

    cls._crew_canvas = get_canvas(window=frame, **CREW_CANVAS_KWARGS)
    cls._city_canvas = get_canvas(window=frame, **CITY_CANVAS_KWARGS)

    crew_input = get_input(window=frame, **CREW_INPUT_COORDS)
    setattr(cls, f'_{category}_crew_input', crew_input)

    city_input = get_input(window=frame, **CITY_INPUT_COORDS)
    setattr(cls, f'_{category}_city_input', city_input)

    cls._register_button = get_register_button(cls=cls, window=frame)
    cls._unregister_button = get_unregister_button(cls=cls, window=frame)

    cls._tab_control.add(frame, text=category)
    clean_category_input(cls=cls)


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
