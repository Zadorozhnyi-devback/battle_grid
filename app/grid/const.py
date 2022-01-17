# settings
FIELDS_FONT_SIZES = {'name': 40, 'crew': 30, 'city': 30}
FONT_PATH = 'static/fonts/Gidole-Regular.ttf'
Y_INDENT_BETWEEN_CARDS = 155
COORDS_RIGHT_8 = {'y_axis': 0, 'x_axis': 1400}
COORDS_LEFT_8 = {'y_axis': 0, 'x_axis': 0}
RECTANGLE_COORDS = (10, 15, 340, 155)
TEXT_XY = (20, 20)
IMAGE = (340, 154)


# aliases
Y_AXIS = 'y_axis'
X_AXIS = 'x_axis'
X = 0
Y = 1

# for test
B_BOYS = list()
for index in range(1, 17):
    B_BOYS.append(
        {'name': f'boy{index}', 'crew': 'some crew', 'city': 'Cicity'}
    )
