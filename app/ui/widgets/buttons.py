import getpass
from pathlib import Path
from tkinter import Tk, Label, Button, Frame, filedialog

from app.ui.validators import validate_category_existing
from settings.ui.const import (
    BUTTON_TEXT_COLOR, CREATE_BUTTON_TITLE, DESTINATION_BUTTON_SIZE,
    CREATE_BUTTON_SIZE, CREATE_BUTTON_COORDS, DESTINATION_BUTTON_COORDS,
    ADD_TAB_BUTTON_TEXT, ADD_TAB_BUTTON_SIZE, ADD_TAB_BUTTON_COORDS,
    DESTINATION_BUTTON_TITLE, DEFAULT_DOWNLOAD_PATH, CURR_PATH,
)


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
        text=f'{CURR_PATH}: {destination_path}'
    )


def get_destination_button(
    main_window: Tk, current_path_label: Label, destination_path: str
) -> Button:
    button = Button(
        master=main_window, text=DESTINATION_BUTTON_TITLE,
        width=DESTINATION_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=(
            lambda
            window=main_window,
            curr_path_label=current_path_label,
            path=destination_path:
                clicked_choose_dir(
                    main_window=window,
                    curr_path_label=curr_path_label,
                    destination_path=path
                )
        )
    )
    button.grid(**DESTINATION_BUTTON_COORDS, sticky='W')
    return button


def clicked_generate_grid(cls) -> None:
    tab_control = cls._tab_control
    current_tab = tab_control.tab(tab_control.select(), 'text')


def get_create_button(cls) -> Button:
    button = Button(
        master=cls._window, text=CREATE_BUTTON_TITLE, width=CREATE_BUTTON_SIZE,
        fg=BUTTON_TEXT_COLOR,
        command=lambda c=cls: clicked_generate_grid(cls=c)
    )
    button.grid(CREATE_BUTTON_COORDS)
    return button


def clicked_add_tab(cls):
    if validate_category_existing(cls=cls):
        category = cls._new_category.get()
        frame = Frame(master=cls._window)
        cls._tab_control.add(frame, text=category)
        cls._categories[category] = {
            'grid_size': cls._selected_grid_size.get(),
            'type': cls._selected_category_type.get(),  # crew or single
            'people': list()
        }
        print(cls._categories[category])


# categories = {
#     'breaking': {
#         'grid_size': int,
#         'type': str,  # crew or single
#         'people': list(dict())
#     }
# }

def get_add_tab_button(cls) -> Button:
    button = Button(
        master=cls._window, text=ADD_TAB_BUTTON_TEXT,
        width=ADD_TAB_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda c=cls: clicked_add_tab(cls=c)
    )
    button.grid(ADD_TAB_BUTTON_COORDS)
    return button
