from typing import Dict

from grid.const import (
    COORDS_LEFT_16_8, COORDS_RIGHT_16_8, COORDS_LEFT_16_4,
    COORDS_RIGHT_16_4, COORDS_RIGHT_16_2, COORDS_LEFT_16_2, COORDS_CENTER_16,
    Y_INDENT_BETWEEN_BLANKS_16_4, Y_INDENT_BETWEEN_BLANKS_16_2,
    Y_INDEN_BEETWEEN_BLANKS_CENTER_16, Y_INDENT_BETWEEN_CARDS_16_8
)


def get_indent_for_16(index: int, squares: str) -> int:
    if squares == 'cards':
        indent = Y_INDENT_BETWEEN_CARDS_16_8
    else:  # blanks
        if index < 8:
            indent = Y_INDENT_BETWEEN_BLANKS_16_4
        elif index < 12:
            indent = Y_INDENT_BETWEEN_BLANKS_16_2
        else:
            indent = Y_INDEN_BEETWEEN_BLANKS_CENTER_16
    return indent


def get_coords_for_16(index: int, squares: str) -> Dict[str, int]:
    if squares == 'cards':
        coords = COORDS_LEFT_16_8 if index < 8 else COORDS_RIGHT_16_8
    else:  # blanks
        if index < 8:
            coords = COORDS_RIGHT_16_4 if index >= 4 else COORDS_LEFT_16_4
        elif index < 12:
            coords = COORDS_LEFT_16_2 if index < 10 else COORDS_RIGHT_16_2
        else:
            coords = COORDS_CENTER_16
    return coords
