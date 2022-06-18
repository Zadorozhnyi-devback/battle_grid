from apps.ui.handlers.savers import save_categories
from apps.ui.validators import validate_for_create_category

from apps.ui.widgets.tab_control.windows import create_new_tab


__all__ = (
    'create_category'
)


def create_category(self) -> None:
    if validate_for_create_category(self) is True:
        create_new_tab(self)

        self._add_category_toplevel.destroy()
        delattr(self, '_add_category_toplevel')

        self._window.focus_force()

        save_categories(self)
