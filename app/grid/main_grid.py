from app.grid.const import get_boys
from app.grid.handlers.common import (
    get_created_image, get_created_draw, get_created_font,
    save_image, create_cards, create_blanks, paste_event_image
)
from settings.grid.common import IMAGE_PATH

category = 'Brkrzz'


class BattleGrid:
    def __init__(self) -> None:
        self._main_image = get_created_image(x=1754, y=1249, color='white')
        self._draw = get_created_draw(image=self._main_image)
        self._grid_size = 32
        self._sex = 'm'  # and 'f'
        self._font = get_created_font(grid_size=self._grid_size)
        self._people = get_boys(grid_size=self._grid_size)
        self.main()

    def main(self) -> None:
        create_cards(
            people=self._people, grid_size=self._grid_size,
            main_image=self._main_image, font=self._font, sex=self._sex
        )
        create_blanks(
            people=self._people, grid_size=self._grid_size,
            main_image=self._main_image
        )
        paste_event_image(
            grid_size=self._grid_size, main_image=self._main_image
        )
        save_image(image=self._main_image, image_path=IMAGE_PATH)
