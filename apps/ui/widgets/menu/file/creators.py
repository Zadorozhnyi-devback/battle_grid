from tkinter import Menu

from .event.create.toplevel.handlers import create_new_event
from .event.open.handlers import open_event


__all__ = (
    'create_file_menu',
)


def create_file_menu(self) -> None:
    self._file_menu = Menu(master=self._menu_bar)

    menus = [
        {'label': 'New', 'command': lambda: create_new_event(self)},
        {'label': 'Open...', 'command': lambda: open_event(self)},
    ]

    for menu in menus:
        self._file_menu.add_command(
            label=menu['label'],
            command=menu['command']
        )

    self._file_menu.add_separator()

    self._menu_bar.add_cascade(
        label='File',
        menu=self._file_menu,
        underline=0
    )
