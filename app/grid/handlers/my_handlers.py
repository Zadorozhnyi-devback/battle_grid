import os
from typing import Dict, Union, Tuple

from PIL import Image, ImageDraw, ImageFont

from grid.const import (
    FONT_PATH, FONT_SIZE_16, FONT_SIZE_8, FONT_SIZE_32, Y_AXIS, X_AXIS
)
from grid.handlers.for_16 import (
    get_coords_for_16, get_indent_for_16, get_params_for_16
)
from grid.handlers.for_32 import (
    get_coords_for_32, get_indent_for_32, get_params_for_32
)
from grid.handlers.for_8 import (
    get_coords_for_8, get_indent_for_8, get_params_for_8
)


def get_indent(index: int, grid_size: int, squares: str) -> int:
    if grid_size == 32:
        indent = get_indent_for_32(index=index, squares=squares)
    elif grid_size == 16:
        indent = get_indent_for_16(index=index, squares=squares)
    else:
        indent = get_indent_for_8(index=index, squares=squares)
    return indent


def get_coords(index: int, grid_size: int, squares: str) -> Dict[str, int]:
    if grid_size == 32:
        coords = get_coords_for_32(index=index, squares=squares)
    elif grid_size == 16:
        coords = get_coords_for_16(index=index, squares=squares)
    else:  # for 8
        coords = get_coords_for_8(index=index, squares=squares)
    return coords


def get_params(grid_size: int, squares: str) -> (
    Tuple[Dict[str, Union[Tuple[int], int, str]]]
):
    if grid_size == 32:
        (
            image_params, rectangle_params, text_params
        ) = get_params_for_32(squares=squares)
    elif grid_size == 16:
        (
            image_params, rectangle_params, text_params
        ) = get_params_for_16(squares=squares)
    else:  # 8
        (
            image_params, rectangle_params, text_params
        ) = get_params_for_8(squares=squares)
    return image_params, rectangle_params, text_params


def create_blank(
    main_image: Image, coords: Dict[str, int], grid_size: int, squares: str
) -> None:
    image_params, rectangle_params, _ = get_params(
        grid_size=grid_size, squares=squares
    )
    card_image = get_created_image(**image_params)
    my_draw = ImageDraw.Draw(card_image)
    my_draw.rounded_rectangle(**rectangle_params)
    main_image.paste(card_image, (coords[X_AXIS], coords[Y_AXIS]))


def create_card(
    main_image: Image, font: ImageFont, squares: str,
    person: Dict[str, str], coords: Dict[str, int], grid_size: int
) -> None:
    image_params, rectangle_params, text_params = get_params(
        grid_size=grid_size, squares=squares
    )
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
    # text = 'yoyoyo'
    # text margin: x left, y top in TEXT_PARAMS['xy']: Tuple[int]
    my_draw.text(text=text, font=font, **text_params)

    main_image.paste(card_image, (coords[X_AXIS], coords[Y_AXIS]))


def save_image(image: Image, image_path: str) -> None:
    try:
        image.save(image_path)
    except FileNotFoundError:
        os.mkdir(path=''.join(image_path.split('/')[:-1]))
        image.save(image_path)


def get_created_font(grid_size: int) -> ImageFont:
    if grid_size == 32:
        font = ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE_32)
    elif grid_size == 16:
        font = ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE_16)
    else:  # for 8
        font = ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE_8)
    return font


def get_created_draw(image: Image) -> ImageDraw:
    return ImageDraw.Draw(image)


def get_created_image(x: int, y: int, color: str) -> Image:
    image = Image.new('RGB', (x, y), color)
    return image
