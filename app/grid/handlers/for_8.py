from typing import Dict

from grid.const import (
    COORDS_LEFT_8_4, COORDS_RIGHT_8_4, COORDS_RIGHT_8_2, COORDS_LEFT_8_2,
    COORDS_CENTER_8, Y_INDENT_BETWEEN_CARDS_8_4, Y_INDENT_BETWEEN_BLANKS_8_2,
    Y_INDEN_BEETWEEN_BLANKS_CENTER_8
)


def get_coords_for_8(index: int, squares: str) -> Dict[str, int]:
    if squares == 'cards':
        coords = COORDS_LEFT_8_4 if index < 4 else COORDS_RIGHT_8_4
    else:  # blanks
        if index < 4:
            coords = COORDS_RIGHT_8_2 if index >= 2 else COORDS_LEFT_8_2
        else:
            coords = COORDS_CENTER_8
    return coords


def get_indent_for_8(index: int, squares: str) -> int:
    if squares == 'cards':
        indent = Y_INDENT_BETWEEN_CARDS_8_4
    else:  # blanks
        if index < 4:
            indent = Y_INDENT_BETWEEN_BLANKS_8_2
        else:
            indent = Y_INDEN_BEETWEEN_BLANKS_CENTER_8
    return indent
