from typing import List

from apps.grid.const import get_boys
from apps.grid.handlers.common import (
    get_created_image, get_created_draw, get_created_font,
    save_image, create_cards, create_blanks, paste_event_image
)
from app.settings.grid.common import IMAGE_PATH


__all__ = 'BattleGrid',


class BattleGrid:
    def __init__(
        self,
        participants: List[dict],
        grid_size: int,
    ) -> None:
        self._main_image = get_created_image(x=1754, y=1249, color='white')
        self._draw = get_created_draw(image=self._main_image)
        self._grid_size = int(grid_size)
        self._font = get_created_font(grid_size=self._grid_size)
        self._participants = participants
        # self._participants = get_boys(grid_size=self._grid_size)

    def generate(self) -> None:
        create_cards(
            participants=self._participants, grid_size=self._grid_size,
            main_image=self._main_image, font=self._font
        )
        create_blanks(grid_size=self._grid_size, main_image=self._main_image)
        paste_event_image(
            grid_size=self._grid_size, main_image=self._main_image
        )
        save_image(image=self._main_image, image_path=IMAGE_PATH)
