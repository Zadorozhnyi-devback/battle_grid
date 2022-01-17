import os
from typing import Dict, Tuple

from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont

from grid.const import (
    FIELDS_FONT_SIZES, FONT_PATH, Y_AXIS, X_AXIS, Y, X, IMAGE,
    RECTANGLE_COORDS, TEXT_XY
)


def get_card(
    main_image: Image, fonts: Dict[str, FreeTypeFont],
    person: Dict[str, str], coords: Dict[str, Tuple[int]]
) -> Image:
    card_image = get_image(x=IMAGE[X], y=IMAGE[Y], color='white')
    my_draw = ImageDraw.Draw(card_image)
    # angles: x left, y top, x right, y bottom (size: 330x140)
    my_draw.rounded_rectangle(
        xy=RECTANGLE_COORDS, width=5, radius=10, fill='white', outline='black'
    )
    text = '\n'.join(
        [
            f'{field.capitalize()}: {value.capitalize()}'
            for field, value in person.items()
        ]
    )
    # text margin: x left, y top
    my_draw.text(xy=TEXT_XY, text=text, font=fonts['crew'], fill='black')
    main_image.paste(card_image, (coords[X_AXIS], coords[Y_AXIS]))
    return card_image


def save_image(image: Image, image_path: str) -> None:
    try:
        image.save(image_path)
    except FileNotFoundError:
        os.mkdir(path=''.join(image_path.split('/')[:-1]))
        image.save(image_path)


def get_fonts() -> Dict[str, FreeTypeFont]:
    fonts = {
        field: ImageFont.truetype(font=FONT_PATH, size=size)
        for field, size
        in FIELDS_FONT_SIZES.items()
    }
    return fonts


def get_draw(image: Image) -> ImageDraw:
    return ImageDraw.Draw(image)


def get_image(x: int, y: int, color: str) -> Image:
    image = Image.new('RGB', (x, y), color)
    return image
