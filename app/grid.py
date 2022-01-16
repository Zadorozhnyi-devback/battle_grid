from handlers.my_handlers import get_image, get_draw, get_fonts, draw_text, \
    save_image

event_name = '5 Points'
category = 'Brkrzz'
boy1 = {
    'nickname': 'Kizyak', 'crew': 'Sopel style', 'city': 'Gopa city'
}
boy2 = {
    'nickname': 'Huilo', 'crew': 'Huli ne huilo', 'city': 'Huli hu city'
}
image_path = 'downloads/output.jpg'


class BattleGrid:
    def __init__(self) -> None:
        self._image = get_image()
        self._draw = get_draw(image=self._image)
        self._fonts = get_fonts()
        self._people = [boy1, boy2]
        self.main()

    def main(self, x: int = 10, y: int = 10) -> None:
        for person in self._people:
            draw_text(
                draw=self._draw, fonts=self._fonts, person=person, x=x, y=y
            )
            x += 160
        save_image(image=self._image, image_path=image_path)

        # self._image.save(output_image)


if __name__ == '__main__':
    BattleGrid()
