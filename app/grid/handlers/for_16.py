from typing import Dict, Tuple, Union

from settings.configs.for_16 import (
    CARD_IMAGE_PARAMS_16, RECTANGLE_PARAMS_16,
    SMALL_IMAGE_PARAMS_16, SMALL_RECTANGLE_PARAMS_16, TEXT_PARAMS_16,
    Y_INDENT_BETWEEN_CARDS_16_8, Y_INDENT_BETWEEN_BLANKS_16_4,
    Y_INDEN_BEETWEEN_BLANKS_CENTER_16, Y_INDENT_BETWEEN_BLANKS_16_2,
    COORDS_LEFT_16_8, COORDS_RIGHT_16_8, COORDS_RIGHT_16_4, COORDS_LEFT_16_4,
    COORDS_LEFT_16_2, COORDS_RIGHT_16_2, COORDS_CENTER_16
)


def get_params_for_16(squares: str) -> (
    Tuple[Union[
        Dict[str, Union[int, str]],
        Dict[str, Union[Tuple[int], int, str]]
    ]]
):
    if squares == 'cards':
        image_params = CARD_IMAGE_PARAMS_16
        rectangle_params = RECTANGLE_PARAMS_16
    else:
        image_params = SMALL_IMAGE_PARAMS_16
        rectangle_params = SMALL_RECTANGLE_PARAMS_16
    text_params = TEXT_PARAMS_16
    return image_params, rectangle_params, text_params


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
