import os
from typing import Dict

from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont

from const import FIELDS_FONT_SIZES, FONT_NAME


def save_image(image: Image, image_path: str) -> None:
    try:
        image.save(image_path)
    except FileNotFoundError:
        os.mkdir(path=''.join(image_path.split('/')[:-1]))
        image.save(image_path)


def draw_text(
    draw: ImageDraw, fonts: Dict[str, FreeTypeFont],
    person: Dict[str, str], x: int, y: int
) -> None:
    for field, font in fonts.items():
        draw.text(
            xy=(y, x), font=font, fill='black',
            text=f"{person.get(field, '-')}\n",
        )
        increase = 40 if field == 'crew' else 50
        x += increase


def get_fonts() -> Dict[str, FreeTypeFont]:
    fonts = {
        field: ImageFont.truetype(font=FONT_NAME, size=size)
        for field, size
        in FIELDS_FONT_SIZES.items()
    }
    return fonts


def get_draw(image: Image) -> ImageDraw:
    return ImageDraw.Draw(image)


def get_image() -> Image:
    image = Image.new('RGB', (1754, 1249), 'white')
    return image
