__all__ = (
    'get_selected_tab_title',
)


def get_selected_tab_title(self) -> str:
    selected_tab = self._tab_control.select()
    if selected_tab:
        category = self._tab_control.tab(selected_tab, 'text')
        return category
