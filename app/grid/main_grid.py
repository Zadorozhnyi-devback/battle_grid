from grid.const import (
    Y_INDENT_BETWEEN_CARDS, Y_AXIS, B_BOYS,
    COORDS_LEFT_8, COORDS_RIGHT_8, IMAGE_PATH
)
from grid.handlers.my_handlers import (
    create_image, create_draw, create_font, save_image, create_card
)


event_name = '5 Points'
category = 'Brkrzz'


class BattleGrid:
    def __init__(self) -> None:
        self._main_image = create_image(x=1754, y=1249, color='white')
        self._draw = create_draw(image=self._main_image)
        self._font = create_font()
        self._people = B_BOYS
        self.main()

    def _create_cards(self) -> None:
        for index, person in enumerate(self._people):
            coords = COORDS_LEFT_8 if index < 8 else COORDS_RIGHT_8
            card = create_card(
                main_image=self._main_image, font=self._font,
                person=person, coords=coords
            )
            setattr(self, f"_{person.get('name')}_card", card)
            coords[Y_AXIS] += Y_INDENT_BETWEEN_CARDS

    def main(self) -> None:
        self._create_cards()
        save_image(image=self._main_image, image_path=IMAGE_PATH)
