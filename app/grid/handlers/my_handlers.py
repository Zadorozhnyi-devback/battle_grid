import os
from typing import Dict, Tuple

from PIL import Image, ImageDraw, ImageFont

from grid.const import (
    FONT_PATH, Y_AXIS, X_AXIS, RECTANGLE_PARAMS,
    CARD_IMAGE_PARAMS, FONT_SIZE, TEXT_PARAMS
)


def create_card(
    main_image: Image, font: ImageFont,
    person: Dict[str, str], coords: Dict[str, Tuple[int]]
) -> Image:
    card_image = create_image(**CARD_IMAGE_PARAMS)
    my_draw = ImageDraw.Draw(card_image)
    # angles: x left, y top, x right, y bottom (size: 330x140)
    my_draw.rounded_rectangle(**RECTANGLE_PARAMS)
    text = '\n'.join(
        [
            f'{field.capitalize()}: {value.capitalize()}'
            for field, value in person.items()
        ]
    )
    # text margin: x left, y top in TEXT_PARAMS
    my_draw.text(text=text, font=font, **TEXT_PARAMS)
    main_image.paste(card_image, (coords[X_AXIS], coords[Y_AXIS]))
    return card_image


def save_image(image: Image, image_path: str) -> None:
    try:
        image.save(image_path)
    except FileNotFoundError:
        os.mkdir(path=''.join(image_path.split('/')[:-1]))
        image.save(image_path)


def create_font() -> ImageFont:
    font = ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE)
    return font


def create_draw(image: Image) -> ImageDraw:
    return ImageDraw.Draw(image)


def create_image(x: int, y: int, color: str) -> Image:
    image = Image.new('RGB', (x, y), color)
    return image
