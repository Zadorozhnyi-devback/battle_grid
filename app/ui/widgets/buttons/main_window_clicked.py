import getpass
import json
from pathlib import Path
from tkinter import (
    messagebox, Tk, Label, filedialog, NORMAL, DISABLED, END, TclError
)
from typing import Dict, Union, List

from app.ui.const import BEGINNING
from app.ui.handlers import remove_old_categories, clean_category_input
from app.ui.validators import (
    validate_category_existing, validate_event_name_exist, validate_event_input
)
from app.ui.widgets.buttons.after_click_creators import (
    create_make_new_event_button, create_rename_event_button
)
from app.ui.widgets.common import get_selected_tab_title
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels import change_text_canvas, get_canvas
from app.ui.widgets.windows import create_new_tab
from settings.ui.const import (
    DEFAULT_DOWNLOAD_PATH, CURRENT_PATH, EVENT_NAME_TITLE_CANVAS_KWARGS,
    EVENT_NAME_INPUT_COORDS
)


def clicked_add_tab(cls):
    if validate_event_name_exist(cls=cls):
        if validate_category_existing(cls=cls):
            create_new_tab(cls=cls)


def clicked_remove_tab(cls) -> None:
    selected_tab = cls._tab_control.select()
    category = get_selected_tab_title(cls=cls)
    answer = messagebox.askyesno(
        message=f"delete category '{category}'?"
    )
    if answer:
        cls._tab_control.forget(selected_tab)
        cls._categories.pop(category)


def clicked_generate_grid(cls) -> None:
    # TODO: here gonna init BattleGrid class instance
    tab_control = cls._tab_control
    current_tab = tab_control.tab(tab_control.select(), 'text')


def clicked_choose_dir(
    main_window: Tk, curr_path_label: Label,
    destination_path: str = DEFAULT_DOWNLOAD_PATH
) -> None:
    directory = filedialog.askdirectory(
        # gonna work on mac, have to check for windows and linux
        # initialdir=os.path.normpath("C://") try on Windows
        parent=main_window,  # костыль для возврата фокуса в инпут после
        initialdir=f'/Users/{getpass.getuser()}/'
    )
    if directory:
        destination_path = str(Path(directory).resolve())
    curr_path_label.configure(
        text=f'{CURRENT_PATH}: {destination_path}'
    )


def clicked_save_event_name(cls) -> None:
    if validate_event_input(cls=cls):
        print('alright')
        cls._event_name = cls._event_name_input.get()

        cls._event_name_title = get_canvas(
            window=cls._window, **EVENT_NAME_TITLE_CANVAS_KWARGS,
            text=cls._event_name
        )
        cls._event_name_input.destroy()
        cls._save_event_name_button.destroy()

        create_make_new_event_button(cls=cls, frame=cls._buttons_frame)
        create_rename_event_button(cls=cls, frame=cls._buttons_frame)

        change_text_canvas(
            canvas=cls._main_canvas,
            text=f"event '{cls._event_name}' was created"
        )
        print('finish save event name')


def create_loaded_categories(
    cls, json_data: Dict[str, Dict[str, Union[str, List[Dict[str, str]]]]]
) -> None:
    for category, data in json_data.items():
        cls._category_input.insert(BEGINNING, category)
        cls._selected_category_type.set(data['type'])
        cls._selected_grid_size.set(data['grid_size'])

        create_new_tab(cls=cls)

        cls._categories[category]['participants'] = data['participants']

        participants = [i for i in data['text_widget'].split('\n') if i]

        text_widget = cls._categories[category]['text_widget']
        text_widget.configure(state=NORMAL)
        [text_widget.insert(END, f'{string}\n') for string in participants]
        text_widget.configure(state=DISABLED)

        clean_category_input(cls=cls)
    print('created')


def clicked_open_event(cls) -> None:
    event_json = filedialog.askopenfilename(
        parent=cls._window,  # для возврата фокуса в инпут после
        initialdir=(
            f'/Users/{getpass.getuser()}/PycharmProjects/battle_grid/events/'
        )
    )
    if event_json:
        clean_category_input(cls=cls)
        if hasattr(cls, '_event_name_title'):
            try:
                cls._event_name_title.destroy()
            except TclError:
                pass
            delattr(cls, '_event_name_title')
        cls._event_name_input.destroy()
        cls._event_name_input = get_input(
            window=cls._window, **EVENT_NAME_INPUT_COORDS
        )
        cls._event_name_input.insert(
            BEGINNING, event_json.split('/')[-1].split('_')[0]
        )

        clicked_save_event_name(cls=cls)
        change_text_canvas(
            canvas=cls._main_canvas,
            text=f"event '{cls._event_name}' was loaded"
        )

        with open(file=event_json, encoding='utf-8') as event_file:
            file_data = json.load(event_file)

        remove_old_categories(cls=cls)
        create_loaded_categories(cls=cls, json_data=file_data)
