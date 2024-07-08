from tkinter import Menu

from apps.ui.widgets.menu.handlers import disable_menu

from .create import create_add_category_toplevel


__all__ = (
    'create_category_menu',
)


def create_category_menu(self) -> None:
    self._category_menu = Menu(master=self._menu_bar)

    menus = [
        {
            'label': 'Add',
            'command': lambda: create_add_category_toplevel(self)
        },
    ]

    for menu in menus:
        self._category_menu.add_command(
            label=menu['label'],
            command=menu['command']
        )

    self._category_menu.add_separator()

    self._menu_bar.add_cascade(
        label='Category',
        menu=self._category_menu,
        underline=0
    )

    disable_menu(self, menu='Category')
