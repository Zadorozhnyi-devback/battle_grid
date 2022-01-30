from grid.const import Y_AXIS, IMAGE_PATH, get_boys
from grid.handlers.my_handlers import (
    get_created_image, get_created_draw, get_created_font,
    save_image, create_card, create_blank, get_coords, get_indent
)


event_name = '5 Points'
category = 'Brkrzz'


class BattleGrid:
    def __init__(self) -> None:
        self._main_image = get_created_image(x=1754, y=1249, color='white')
        self._draw = get_created_draw(image=self._main_image)
        self._grid_size = 32
        self._font = get_created_font(grid_size=self._grid_size)
        self._people = get_boys(grid_size=self._grid_size)
        self.main()

    def _create_cards(self, _squares: str = 'cards') -> None:
        for index, person in enumerate(self._people):
            coords = get_coords(
                index=index, grid_size=self._grid_size, squares=_squares
            )
            create_card(
                main_image=self._main_image, font=self._font,
                person=person, coords=coords, grid_size=self._grid_size,
                squares=_squares
            )
            # maybe don't need
            # setattr(self, f"_{person.get('name')}_card", card)
            indent = get_indent(
                index=index, grid_size=self._grid_size, squares=_squares
            )
            coords[Y_AXIS] += indent

    def _create_blanks(self, _squares: str = 'blanks') -> None:
        for index in range(len(self._people) - 1):
            coords = get_coords(
                index=index, grid_size=self._grid_size, squares=_squares
            )
            create_blank(
                main_image=self._main_image, squares=_squares,
                coords=coords, grid_size=self._grid_size
            )
            indent = get_indent(
                index=index, grid_size=self._grid_size, squares=_squares)
            coords[Y_AXIS] += indent

    def main(self) -> None:
        self._create_cards()
        self._create_blanks()
        save_image(image=self._main_image, image_path=IMAGE_PATH)
