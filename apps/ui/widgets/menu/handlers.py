from tkinter import DISABLED, NORMAL


__all__ = (
    'disable_menu',
    'enable_menu',
)


def disable_menu(self, menu: str) -> None:
    self._menu_bar.entryconfig(menu, state=DISABLED)


def enable_menu(self, menu: str) -> None:
    self._menu_bar.entryconfig(menu, state=NORMAL)
