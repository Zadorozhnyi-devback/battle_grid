from grid.const import (
    Y_INDENT_BETWEEN_CARDS, Y_AXIS, B_BOYS, COORDS_LEFT_8, COORDS_RIGHT_8
)
from grid.handlers.my_handlers import (
    get_image, get_draw, get_fonts, save_image, get_card
)


event_name = '5 Points'
category = 'Brkrzz'
image_path = 'downloads/output.jpg'


class BattleGrid:
    def __init__(self) -> None:
        self._main_image = get_image(x=1754, y=1249, color='white')
        self._draw = get_draw(image=self._main_image)
        self._fonts = get_fonts()
        self._people = B_BOYS
        self.main()

    def _create_cards(self) -> None:
        for index, person in enumerate(self._people):
            coords = COORDS_LEFT_8 if index < 8 else COORDS_RIGHT_8
            card = get_card(
                main_image=self._main_image, fonts=self._fonts,
                person=person, coords=coords
            )
            setattr(self, f"_{person.get('name')}_card", card)
            coords[Y_AXIS] += Y_INDENT_BETWEEN_CARDS

    def main(self) -> None:
        self._create_cards()
        save_image(image=self._main_image, image_path=image_path)
