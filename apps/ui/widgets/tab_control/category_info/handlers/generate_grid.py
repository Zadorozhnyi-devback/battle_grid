__all__ = (
    'generate_grid',
)


def generate_grid(self) -> None:
    # TODO: here gonna init BattleGrid class instance
    tab_control = self._tab_control
    current_tab = tab_control.tab(tab_control.select(), 'text')
