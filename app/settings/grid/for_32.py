# 32
from apps.grid import IntAlias

IMAGE_32 = (200, 70)
SMALL_IMAGE_32 = (200, 75)
SMALL_RECTANGLE_COORDS_32 = (0, 0, 200, 75)
RECTANGLE_COORDS_32 = (0, 0, 200, 70)
FONT_SIZE_32 = 18
TEXT_XY_32 = (25, 5)
TEXT_PARAMS_32 = {'xy': TEXT_XY_32, 'fill': 'black'}
EVENT_IMAGE_SIZE_32 = (400, 240)
EVENT_IMAGE_COORDS_32 = (690, 30)
EVENT_IMAGE_SIZE_8 = (440, 260)
EVENT_IMAGE_COORDS_8 = (675, 30)

Y_INDENT_BETWEEN_CARDS_32_16 = 77
Y_INDENT_BETWEEN_BLANKS_32_8 = 153
Y_INDENT_BETWEEN_BLANKS_32_4 = 307
Y_INDENT_BETWEEN_BLANKS_32_2 = 615
Y_INDEN_BEETWEEN_BLANKS_CENTER_32 = 190

COORDS_LEFT_32_16 = {'y_axis': 12, 'x_axis': 10}
COORDS_RIGHT_32_16 = {'y_axis': 12, 'x_axis': 1544}
COORDS_LEFT_32_8 = {'y_axis': 50, 'x_axis': 225}
COORDS_RIGHT_32_8 = {'y_axis': 50, 'x_axis': 1330}
COORDS_LEFT_32_4 = {'y_axis': 127, 'x_axis': 440}
COORDS_RIGHT_32_4 = {'y_axis': 127, 'x_axis': 1115}
COORDS_LEFT_32_2 = {'y_axis': 282, 'x_axis': 658}
COORDS_RIGHT_32_2 = {'y_axis': 282, 'x_axis': 900}
COORDS_CENTER_32 = {'y_axis': 400, 'x_axis': 780}

# person, location, crew
ICON_SIZES_32 = [[(25, 20)], [(25, 20)], [(25, 20)]]
ICONS_COORDS_32 = [(6, 5), (5, 25), (7, 45)]

SMALL_RECTANGLE_PARAMS_32 = {
    'xy': SMALL_RECTANGLE_COORDS_32, 'width': 5, 'radius': 10,
    'fill': 'white', 'outline': 'black'
}
RECTANGLE_PARAMS_32 = {
    'xy': RECTANGLE_COORDS_32, 'width': 5, 'radius': 10,
    'fill': 'white', 'outline': 'black'
}
CARD_IMAGE_PARAMS_32 = {
    'x': IMAGE_32[IntAlias.X], 'y': IMAGE_32[IntAlias.Y], 'color': 'white'
}
SMALL_IMAGE_PARAMS_32 = {
    'x': SMALL_IMAGE_32[IntAlias.X],
    'y': SMALL_IMAGE_32[IntAlias.Y], 'color': 'white'
}
