# 16
from apps.grid import IntAlias

IMAGE_16 = (340, 154)
SMALL_IMAGE_16 = (200, 130)
FONT_SIZE_16 = 38
TEXT_XY_16 = (60, 29)
TEXT_PARAMS_16 = {'xy': TEXT_XY_16, 'fill': 'black'}
EVENT_IMAGE_SIZE_16 = (420, 220)
EVENT_IMAGE_COORDS_16 = (710, 30)

Y_INDENT_BETWEEN_CARDS_16_8 = 155
Y_INDENT_BETWEEN_BLANKS_16_4 = 310
Y_INDENT_BETWEEN_BLANKS_16_2 = 620
Y_INDEN_BEETWEEN_BLANKS_CENTER_16 = 180

COORDS_RIGHT_16_8 = {'y_axis': 0, 'x_axis': 1400}
COORDS_LEFT_16_8 = {'y_axis': 0, 'x_axis': 0}
COORDS_LEFT_16_4 = {'y_axis': 85, 'x_axis': 355}
COORDS_RIGHT_16_4 = {'y_axis': 95, 'x_axis': 1185}
COORDS_LEFT_16_2 = {'y_axis': 240, 'x_axis': 570}
COORDS_RIGHT_16_2 = {'y_axis': 244, 'x_axis': 975}
COORDS_CENTER_16 = {'y_axis': 374, 'x_axis': 775}

ICON_SIZES_16 = [[(50, 45)], [(50, 45)], [(50, 43)]]
ICONS_COORDS_16 = [(17, 20), (15, 65), (21, 107)]

RECTANGLE_COORDS_16 = (10, 15, 340, 155)  # (size: 330x140)
SMALL_RECTANGLE_COORDS_16 = (10, 15, 200, 130)

RECTANGLE_PARAMS_16 = {
    'xy': RECTANGLE_COORDS_16, 'width': 5, 'radius': 10,
    'fill': 'white', 'outline': 'black'
}
SMALL_RECTANGLE_PARAMS_16 = {
    'xy': SMALL_RECTANGLE_COORDS_16, 'width': 5, 'radius': 10,
    'fill': 'white', 'outline': 'black'
}
CARD_IMAGE_PARAMS_16 = {
    'x': IMAGE_16[IntAlias.X], 'y': IMAGE_16[IntAlias.Y], 'color': 'white'
}
SMALL_IMAGE_PARAMS_16 = {
    'x': SMALL_IMAGE_16[IntAlias.X],
    'y': SMALL_IMAGE_16[IntAlias.Y], 'color': 'white'
}
