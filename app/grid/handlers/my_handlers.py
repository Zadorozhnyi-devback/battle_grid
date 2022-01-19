import os
from typing import Dict, Union, Tuple

from PIL import Image, ImageDraw, ImageFont

from grid.const import (
    FONT_PATH, FONT_SIZE_16, Y_AXIS, X_AXIS, TEXT_PARAMS,
    SMALL_RECTANGLE_PARAMS_16, SMALL_IMAGE_PARAMS_16,
    FONT_SIZE_8, SMALL_IMAGE_PARAMS_8, SMALL_RECTANGLE_PARAMS_8
)
from grid.handlers.for_16 import get_coords_for_16, get_indent_for_16
from grid.handlers.for_8 import get_coords_for_8, get_indent_for_8


def get_indent(index: int, grid_size: int, squares: str) -> int:
    if grid_size == 16:
        indent = get_indent_for_16(index=index, squares=squares)
    else:
        indent = get_indent_for_8(index=index, squares=squares)
    return indent


def get_coords(index: int, grid_size: int, squares: str) -> Dict[str, int]:
    if grid_size == 16:
        coords = get_coords_for_16(index=index, squares=squares)
    else:  # for 8
        coords = get_coords_for_8(index=index, squares=squares)
    return coords


def get_params(
        grid_size: int
) -> (
        Tuple[Union[
            Dict[str, Union[int, str]],
            Dict[str, Union[Tuple[int], int, str]]
        ]]
):
    if grid_size == 16:
        image_params = SMALL_IMAGE_PARAMS_16
        rectangle_params = SMALL_RECTANGLE_PARAMS_16
    else:  # blanks
        image_params = SMALL_IMAGE_PARAMS_8
        rectangle_params = SMALL_RECTANGLE_PARAMS_8
    return image_params, rectangle_params


def create_blank(
    main_image: Image, coords: Dict[str, int], grid_size: int
) -> None:
    image_params, rectangle_params = get_params(grid_size=grid_size)
    card_image = get_created_image(**image_params)
    my_draw = ImageDraw.Draw(card_image)
    my_draw.rounded_rectangle(**rectangle_params)
    main_image.paste(card_image, (coords[X_AXIS], coords[Y_AXIS]))


def create_card(
    main_image: Image, font: ImageFont,
    person: Dict[str, str], coords: Dict[str, int], grid_size: int
) -> None:
    image_params, rectangle_params = get_params(grid_size=grid_size)
    card_image = get_created_image(**image_params)
    my_draw = ImageDraw.Draw(card_image)
    # angles:  x left, y top, x right, y bottom
    my_draw.rounded_rectangle(**rectangle_params)

    text = '\n'.join(
        [
            f'{field.capitalize()}: {value.capitalize()}'
            for field, value in person.items()
        ]
    )
    # text margin: x left, y top in TEXT_PARAMS['xy']: Tuple[int]
    my_draw.text(text=text, font=font, **TEXT_PARAMS)

    main_image.paste(card_image, (coords[X_AXIS], coords[Y_AXIS]))


def save_image(image: Image, image_path: str) -> None:
    try:
        image.save(image_path)
    except FileNotFoundError:
        os.mkdir(path=''.join(image_path.split('/')[:-1]))
        image.save(image_path)


def get_created_font(grid_size: int) -> ImageFont:
    if grid_size == 16:
        font = ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE_16)
    else:  # for 8
        font = ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE_8)
    return font


def get_created_draw(image: Image) -> ImageDraw:
    return ImageDraw.Draw(image)


def get_created_image(x: int, y: int, color: str) -> Image:
    image = Image.new('RGB', (x, y), color)
    return image
