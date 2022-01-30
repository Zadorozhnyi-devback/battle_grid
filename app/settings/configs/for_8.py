from grid.const import IntAlias

# 8
IMAGE_8 = (340, 154)
SMALL_IMAGE_8 = (300, 150)
SMALL_RECTANGLE_COORDS_8 = (10, 15, 300, 150)
RECTANGLE_COORDS_8 = (10, 15, 340, 155)
FONT_SIZE_8 = 35
TEXT_XY_8 = (20, 20)
TEXT_PARAMS_8 = {'xy': TEXT_XY_8, 'fill': 'black'}

Y_INDENT_BETWEEN_CARDS_8_4 = 300
Y_INDENT_BETWEEN_BLANKS_8_2 = 604
Y_INDEN_BEETWEEN_BLANKS_CENTER_8 = 230

COORDS_LEFT_8_4 = {'y_axis': 100, 'x_axis': 0}
COORDS_RIGHT_8_4 = {'y_axis': 100, 'x_axis': 1400}
COORDS_RIGHT_8_2 = {'y_axis': 256, 'x_axis': 1094}
COORDS_LEFT_8_2 = {'y_axis': 256, 'x_axis': 350}
COORDS_CENTER_8 = {'y_axis': 325, 'x_axis': 720}

SMALL_RECTANGLE_PARAMS_8 = {
    'xy': SMALL_RECTANGLE_COORDS_8, 'width': 5, 'radius': 10,
    'fill': 'white', 'outline': 'black'
}
RECTANGLE_PARAMS_8 = {
    'xy': RECTANGLE_COORDS_8, 'width': 5, 'radius': 10,
    'fill': 'white', 'outline': 'black'
}
CARD_IMAGE_PARAMS_8 = {
    'x': IMAGE_8[IntAlias.X], 'y': IMAGE_8[IntAlias.Y], 'color': 'white'
}
SMALL_IMAGE_PARAMS_8 = {
    'x': SMALL_IMAGE_8[IntAlias.X],
    'y': SMALL_IMAGE_8[IntAlias.Y], 'color': 'white'
}
