from tkinter import Menu

from .settings.toplevel.creators import create_settings_toplevel


__all__ = (
    'create_battle_grid_menu',
)


def create_battle_grid_menu(self) -> None:
    self._battle_grid_menu = Menu(master=self._menu_bar)

    menus = [
        {
            'label': 'Settings',
            'command': lambda: create_settings_toplevel(self)
        },
        {'label': 'Exit', 'command': self._window.destroy},
    ]

    for menu in menus:
        self._battle_grid_menu.add_command(
            label=menu['label'],
            command=menu['command']
        )

    self._menu_bar.add_cascade(
        label='BattleGrid',
        menu=self._battle_grid_menu,
        underline=0
    )
