import getpass
from pathlib import Path
from tkinter import messagebox, Tk, Label, filedialog

from app.ui.validators import validate_category_existing
from app.ui.widgets.windows import create_new_tab
from settings.ui.const import DEFAULT_DOWNLOAD_PATH, CURR_PATH


def clicked_add_tab(cls):
    if validate_category_existing(cls=cls):
        create_new_tab(cls=cls)


def clicked_remove_tab(cls) -> None:
    selected_tab = cls._tab_control.select()
    category = cls._tab_control.tab(selected_tab, 'text')
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
        text=f'{CURR_PATH}: {destination_path}'
    )
