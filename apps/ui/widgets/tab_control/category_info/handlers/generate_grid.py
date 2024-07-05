from apps.grid.main_grid import BattleGrid
from apps.ui.widgets.tab_control.utils.common import get_selected_tab_title


__all__ = (
    'generate_category_grid',
)


def generate_category_grid(self) -> None:
    category = get_selected_tab_title(self)

    category_data = self._categories[category]

    bg = BattleGrid(
        participants=category_data['participants'],
        grid_size=category_data['grid_size']
    )
    bg.generate()
