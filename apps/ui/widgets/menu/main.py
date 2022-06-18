from tkinter import Menu

from apps.ui.widgets.menu.category.creators import create_category_menu
from apps.ui.widgets.menu.file.creators import create_file_menu
from apps.ui.widgets.menu.battle_grid.creators import create_battle_grid_menu


__all__ = (
    'create_menu_bar',
)


def create_menu_bar(self) -> None:
    self._menu_bar = Menu(master=self._window)
    self._window.config(menu=self._menu_bar)

    create_battle_grid_menu(self)
    create_file_menu(self)
    create_category_menu(self)
