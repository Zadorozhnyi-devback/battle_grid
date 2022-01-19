# aliases
Y_AXIS = 'y_axis'
X_AXIS = 'x_axis'
X = 0
Y = 1

# for test
B_BOYS = list()
# for index in range(1, 17): # for 16
for index in range(1, 9):  # for 8
    B_BOYS.append(
        {'name': f'boy{index}', 'crew': 'some crew', 'city': 'Cicity'}
    )


# settings
IMAGE_PATH = 'output_grids/output.jpg'
FONT_PATH = 'static/fonts/Gidole-Regular.ttf'

# common
TEXT_XY = (20, 20)
TEXT_PARAMS = {'xy': TEXT_XY, 'fill': 'black'}

# 16
IMAGE_16 = (340, 154)
SMALL_IMAGE_16 = (200, 130)
FONT_SIZE_16 = 35

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
CARD_IMAGE_PARAMS_16 = {'x': IMAGE_16[X], 'y': IMAGE_16[Y], 'color': 'white'}
SMALL_IMAGE_PARAMS_16 = {
    'x': SMALL_IMAGE_16[X], 'y': SMALL_IMAGE_16[Y], 'color': 'white'
}


# 8
FONT_SIZE_8 = 35
IMAGE_8 = (340, 154)
SMALL_IMAGE_8 = (300, 150)
SMALL_RECTANGLE_COORDS_8 = (10, 15, 300, 150)

Y_INDENT_BETWEEN_CARDS_8_4 = 300
Y_INDENT_BETWEEN_BLANKS_8_2 = 604
Y_INDEN_BEETWEEN_BLANKS_CENTER_8 = 230

COORDS_LEFT_8_4 = {'y_axis': 100, 'x_axis': 0}
COORDS_RIGHT_8_4 = {'y_axis': 100, 'x_axis': 1443}
COORDS_RIGHT_8_2 = {'y_axis': 256, 'x_axis': 1094}
COORDS_LEFT_8_2 = {'y_axis': 256, 'x_axis': 350}
COORDS_CENTER_8 = {'y_axis': 325, 'x_axis': 720}

SMALL_RECTANGLE_PARAMS_8 = {
    'xy': SMALL_RECTANGLE_COORDS_8, 'width': 5, 'radius': 10,
    'fill': 'white', 'outline': 'black'
}
SMALL_IMAGE_PARAMS_8 = {
    'x': SMALL_IMAGE_8[X], 'y': SMALL_IMAGE_8[Y], 'color': 'white'
}
