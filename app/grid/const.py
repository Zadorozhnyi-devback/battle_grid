from typing import Dict, List

# aliases
Y_AXIS = 'y_axis'
X_AXIS = 'x_axis'
X = 0
Y = 1


def get_boys(grid_size: int) -> List[Dict[str, str]]:  # for test
    bboys = list()
    for index in range(1, grid_size + 1):
        bboys.append(
            {'name': f'boy{index}', 'crew': 'some crew', 'city': 'Cicity'}
        )
    return bboys


# settings
DEFAULT_EVENT_IMAGE_PATH = 'static/5p logo.jpg'
IMAGE_PATH = 'output_grids/output.jpg'
FONT_PATH = 'static/fonts/Gidole-Regular.ttf'

# 16
IMAGE_16 = (340, 154)
SMALL_IMAGE_16 = (200, 130)
FONT_SIZE_16 = 35
TEXT_XY_16 = (20, 20)
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
CARD_IMAGE_PARAMS_8 = {'x': IMAGE_8[X], 'y': IMAGE_8[Y], 'color': 'white'}
SMALL_IMAGE_PARAMS_8 = {
    'x': SMALL_IMAGE_8[X], 'y': SMALL_IMAGE_8[Y], 'color': 'white'
}

# 32
IMAGE_32 = (200, 70)
SMALL_IMAGE_32 = (200, 75)
SMALL_RECTANGLE_COORDS_32 = (0, 0, 200, 75)
RECTANGLE_COORDS_32 = (0, 0, 200, 70)
FONT_SIZE_32 = 18
TEXT_XY_32 = (5, 3)
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

SMALL_RECTANGLE_PARAMS_32 = {
    'xy': SMALL_RECTANGLE_COORDS_32, 'width': 5, 'radius': 10,
    'fill': 'white', 'outline': 'black'
}
RECTANGLE_PARAMS_32 = {
    'xy': RECTANGLE_COORDS_32, 'width': 5, 'radius': 10,
    'fill': 'white', 'outline': 'black'
}
CARD_IMAGE_PARAMS_32 = {'x': IMAGE_32[X], 'y': IMAGE_32[Y], 'color': 'white'}
SMALL_IMAGE_PARAMS_32 = {
    'x': SMALL_IMAGE_32[X], 'y': SMALL_IMAGE_32[Y], 'color': 'white'
}
