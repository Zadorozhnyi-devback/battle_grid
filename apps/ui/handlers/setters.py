__all__ = (
    'set_grid_size',
    'set_category_type'
)


def set_grid_size(self, category: str, grid_size: str) -> None:
    self._categories[category]['grid_size'] = grid_size


def set_category_type(self, category: str, tab_type: str) -> None:
    self._categories[category]['type'] = tab_type
