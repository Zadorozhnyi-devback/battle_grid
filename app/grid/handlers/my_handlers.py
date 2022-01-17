import os
from typing import Dict, List

from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont

from grid.const import FIELDS_FONT_SIZES, FONT_PATH, Y_AXIS


def get_card(
    main_image: Image, fonts: Dict[str, FreeTypeFont],
    person: Dict[str, str], coordinates: List[int]
) -> Image:
    # size for top16 card
    card_image = get_image(x=340, y=154, color='white')
    my_draw = ImageDraw.Draw(card_image)
    # angles: x left, y top, x right, y bottom (size: 330x140)
    my_draw.rounded_rectangle(
        xy=(10, 15, 340, 155), width=5, radius=10,
        fill='white', outline='black'
    )
    text = '\n'.join(
        [
            f'{field.capitalize()}: {value.capitalize()}'
            for field, value in person.items()
        ]
    )
    # text margin: x left, y top
    my_draw.text((20, 20), text, font=fonts['crew'], fill='black')
    main_image.paste(card_image, (0, coordinates[Y_AXIS]))
    return card_image


def save_image(image: Image, image_path: str) -> None:
    try:
        image.save(image_path)
    except FileNotFoundError:
        os.mkdir(path=''.join(image_path.split('/')[:-1]))
        image.save(image_path)


# unused
def draw_text(
    draw: ImageDraw, fonts: Dict[str, FreeTypeFont],
    people: List[Dict[str, str]], x: int = 10, y: int = 10
) -> None:
    for person in people:
        for field, font in fonts.items():
            draw.text(
                xy=(y, x), font=font, fill='black',
                text=f"{person.get(field, '-')}\n", align='center'
            )
            increase = 40 if field == 'crew' else 50
            x += increase
        x += 30


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
