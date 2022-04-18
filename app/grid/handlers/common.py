import os
from typing import Dict, Union, Tuple, List

from PIL import Image, ImageDraw, ImageFont

from app.grid.handlers.for_16 import (
    get_coords_for_16, get_indent_for_16, get_params_for_16
)
from app.grid.handlers.for_32 import (
    get_coords_for_32, get_indent_for_32, get_params_for_32
)
from app.grid.handlers.for_8 import (
    get_coords_for_8, get_indent_for_8, get_params_for_8
)
from app.grid.const import StrAlias, IntAlias
from settings.grid.for_16 import (
    EVENT_IMAGE_SIZE_16, EVENT_IMAGE_COORDS_16, FONT_SIZE_16, ICON_SIZES_16,
    ICONS_COORDS_16
)
from settings.grid.for_32 import (
    EVENT_IMAGE_SIZE_32, EVENT_IMAGE_SIZE_8,
    EVENT_IMAGE_COORDS_32, EVENT_IMAGE_COORDS_8, FONT_SIZE_32, ICON_SIZES_32,
    ICONS_COORDS_32
)
from settings.grid.for_8 import (
    FONT_SIZE_8, ICON_SIZES_8, ICONS_COORDS_8
)
from settings.grid.common import (
    DEFAULT_EVENT_IMAGE_PATH, FONT_PATH, ICONS_PATHS, PERSON_ICON_PATHS
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
        return get_coords_for_32(index=index, squares=squares)
    elif grid_size == 16:
        return get_coords_for_16(index=index, squares=squares)
    else:  # for 8
        return get_coords_for_8(index=index, squares=squares)


def get_params(grid_size: int, squares: str) -> (
    Tuple[Dict[str, Union[Tuple[int], int, str]]]
):
    if grid_size == 32:
        return get_params_for_32(squares=squares)
    elif grid_size == 16:
        return get_params_for_16(squares=squares)
    else:  # 8
        return get_params_for_8(squares=squares)


def get_event_image_size(grid_size: int) -> Tuple[int]:
    if grid_size == 32:
        image_size = EVENT_IMAGE_SIZE_32
    elif grid_size == 16:
        image_size = EVENT_IMAGE_SIZE_16
    else:  # 8
        image_size = EVENT_IMAGE_SIZE_8
    return image_size


def get_event_image_coords(grid_size: int) -> Tuple[int]:
    if grid_size == 32:
        coords = EVENT_IMAGE_COORDS_32
    elif grid_size == 16:
        coords = EVENT_IMAGE_COORDS_16
    else:  # 8
        coords = EVENT_IMAGE_COORDS_8
    return coords


def paste_event_image(
    grid_size: int, main_image: Image, path: str = DEFAULT_EVENT_IMAGE_PATH
) -> None:
    event_image = Image.open(path)
    event_image_coords = get_event_image_coords(grid_size=grid_size)
    event_image_size = get_event_image_size(grid_size=grid_size)
    event_image.thumbnail(event_image_size)

    main_image.paste(
        event_image, event_image_coords, event_image.convert('RGBA')
    )


def create_blank(
    main_image: Image, coords: Dict[str, int], grid_size: int, squares: str
) -> None:
    image_params, rectangle_params, _ = get_params(
        grid_size=grid_size, squares=squares
    )
    card_image = get_created_image(**image_params)
    my_draw = ImageDraw.Draw(card_image)
    my_draw.rounded_rectangle(**rectangle_params)
    main_image.paste(
        card_image, (coords[StrAlias.X_AXIS], coords[StrAlias.Y_AXIS])
    )


def create_blanks(
    people: List[Dict[str, str]], grid_size: int,
    main_image: Image, squares: str = 'blanks'
) -> None:
    for index in range(len(people) - 1):
        coords = get_coords(index=index, grid_size=grid_size, squares=squares)
        create_blank(
            main_image=main_image, squares=squares,
            coords=coords, grid_size=grid_size
        )
        indent = get_indent(index=index, grid_size=grid_size, squares=squares)
        coords[StrAlias.Y_AXIS] += indent


def get_icons_coords(grid_size: int) -> List[Tuple[int]]:
    if grid_size == 32:
        return ICONS_COORDS_32
    elif grid_size == 16:
        return ICONS_COORDS_16
    else:  # 8
        return ICONS_COORDS_8


def get_icons_sizes(grid_size: int) -> List[List[Tuple[int, int]]]:
    if grid_size == 32:
        return ICON_SIZES_32
    elif grid_size == 16:
        return ICON_SIZES_16
    else:  # 8
        return ICON_SIZES_8


def get_icons(
    grid_size: int, sex: str, icon_paths: List[str] = ICONS_PATHS
) -> List['Image']:
    # TODO: what for is check for length of icon_paths
    if len(icon_paths) < 3:
        person = 'boy' if sex == 'm' else 'girl'
        icon_paths.insert(IntAlias.FIRST, PERSON_ICON_PATHS[person])
    icons_sizes = get_icons_sizes(grid_size=grid_size)
    sizes_and_paths = list()
    for index, path in enumerate(icon_paths):
        sizes_and_paths.append([path] + icons_sizes[index])
    icons = list()
    for icon in sizes_and_paths:
        icons.append(Image.open(icon[IntAlias.PATH]))
        icons[IntAlias.CURRENT_ICON].thumbnail(icon[IntAlias.SIZE])
    return icons


def paste_icons_to_card(card_image: Image, sex: str, grid_size: int) -> None:
    icons = get_icons(grid_size=grid_size, sex=sex)
    icons_coords = get_icons_coords(grid_size=grid_size)
    for index in range(3):
        card_image.paste(icons[index], icons_coords[index])


def create_card(
    main_image: Image, font: ImageFont, squares: str,
    person: Dict[str, str], coords: Dict[str, int], grid_size: int, sex: str
) -> None:
    image_params, rectangle_params, text_params = get_params(
        grid_size=grid_size, squares=squares
    )
    card_image = get_created_image(**image_params)
    my_draw = ImageDraw.Draw(card_image)
    # angles:  x left, y top, x right, y bottom
    my_draw.rounded_rectangle(**rectangle_params)

    paste_icons_to_card(card_image=card_image, sex=sex, grid_size=grid_size)

    text = '\n'.join([value.capitalize() for _, value in person.items()])
    # text margin: x left, y top in TEXT_PARAMS['xy']: Tuple[int]
    my_draw.text(text=text, font=font, **text_params)

    main_image.paste(
        card_image, (coords[StrAlias.X_AXIS], coords[StrAlias.Y_AXIS])
    )


def create_cards(
    people: List[Dict[str, str]], grid_size: int, main_image: Image,
    font: ImageFont, sex: str, squares: str = 'cards'
) -> None:
    for index, person in enumerate(people):
        coords = get_coords(index=index, grid_size=grid_size, squares=squares)
        create_card(
            main_image=main_image, font=font, squares=squares,
            person=person, coords=coords, grid_size=grid_size, sex=sex
        )
        # maybe don't need
        # setattr(self, f"_{person.get('name')}_card", card)
        indent = get_indent(index=index, grid_size=grid_size, squares=squares)
        coords[StrAlias.Y_AXIS] += indent


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
