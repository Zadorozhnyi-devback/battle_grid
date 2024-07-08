from typing import Dict, Tuple, Union

from app.settings.grid.for_32 import (
    CARD_IMAGE_PARAMS_32, RECTANGLE_PARAMS_32,
    SMALL_IMAGE_PARAMS_32, SMALL_RECTANGLE_PARAMS_32, TEXT_PARAMS_32,
    Y_INDENT_BETWEEN_CARDS_32_16, Y_INDENT_BETWEEN_BLANKS_32_8,
    Y_INDENT_BETWEEN_BLANKS_32_4, Y_INDENT_BETWEEN_BLANKS_32_2,
    Y_INDEN_BEETWEEN_BLANKS_CENTER_32, COORDS_LEFT_32_16, COORDS_RIGHT_32_16,
    COORDS_RIGHT_32_8, COORDS_LEFT_32_8, COORDS_LEFT_32_4, COORDS_RIGHT_32_4,
    COORDS_RIGHT_32_2, COORDS_LEFT_32_2, COORDS_CENTER_32
)


def get_params_for_32(squares: str) -> (
    Tuple[Union[
        Dict[str, Union[int, str]],
        Dict[str, Union[Tuple[int], int, str]]
    ]]
):
    if squares == 'cards':
        image_params = CARD_IMAGE_PARAMS_32
        rectangle_params = RECTANGLE_PARAMS_32
    else:  # blanks
        image_params = SMALL_IMAGE_PARAMS_32
        rectangle_params = SMALL_RECTANGLE_PARAMS_32
    text_params = TEXT_PARAMS_32
    return image_params, rectangle_params, text_params


def get_indent_for_32(index: int, squares: str) -> int:
    if squares == 'cards':
        indent = Y_INDENT_BETWEEN_CARDS_32_16
    else:  # blanks
        if index < 16:
            indent = Y_INDENT_BETWEEN_BLANKS_32_8
        elif index < 24:
            indent = Y_INDENT_BETWEEN_BLANKS_32_4
        elif index < 28:
            indent = Y_INDENT_BETWEEN_BLANKS_32_2
        else:
            indent = Y_INDEN_BEETWEEN_BLANKS_CENTER_32
    return indent


def get_coords_for_32(index: int, squares: str) -> Dict[str, int]:
    if squares == 'cards':
        coords = COORDS_LEFT_32_16 if index < 16 else COORDS_RIGHT_32_16
    else:  # blanks
        if index < 16:
            coords = COORDS_RIGHT_32_8 if index >= 8 else COORDS_LEFT_32_8
        elif index < 24:
            coords = COORDS_LEFT_32_4 if index < 20 else COORDS_RIGHT_32_4
        elif index < 28:
            coords = COORDS_LEFT_32_2 if index < 26 else COORDS_RIGHT_32_2
        else:
            coords = COORDS_CENTER_32
    return coords
