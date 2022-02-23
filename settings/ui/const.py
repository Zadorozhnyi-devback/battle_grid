# aliases
CURR_PATH = 'load folder'
MAIN_CANVAS_TEXT = 'welcome to battle grid!'
NICKNAME_CANVAS_TEXT = 'nick:'
CITY_CANVAS_TEXT = 'city:'
NEW_CATEGORY_CANVAS_TEXT = 'category:'
CREW_CANVAS_TEXT = 'crew:'
GRID_SIZE_CANVAS_TEXT = 'grid:'

# buttons
DESTINATION_BUTTON_TITLE = 'choose folder'
CREATE_BUTTON_TITLE = 'register'
ADD_TAB_BUTTON_TEXT = 'add category'
REMOVE_TAB_BUTTON_TEXT = 'remove category'


# errors


# settings
# common
DEFAULT_DOWNLOAD_PATH = 'output_grids'
WINDOW_TITLE = 'battle grid'
WINDOW_SIZE = '800x600'
TAB_CONTROL_WINDOW_SIZE = {'width': 746, 'height': 300}
MY_FONT = 'Arial Bold'
DEFAULT_FONT_SIZE = 14
BUTTON_TEXT_COLOR = 'red'

# main window
DEFAULT_GRID_SIZE = '8'
DEFAULT_CATEGORY_TYPE = 'single'

DESTINATION_BUTTON_SIZE = '12'
DESTINATION_BUTTON_COORDS = {'row': 5, 'column': 1}
CURR_PATH_LABEL_COORDS = {'row': 4, 'column': 0}

ADD_TAB_BUTTON_SIZE = '10'
ADD_TAB_BUTTON_COORDS = {'row': 8, 'column': 2}
REMOVE_TAB_BUTTON_SIZE = '12'
REMOVE_TAB_BUTTON_COORDS = {'row': 8, 'column': 3}

GRID_SIZE_RADIO_FRAME_COORDS = {'row': 7, 'column': 1}
GRID_SIZE_CANVAS_KWARGS = {
    'row': 7, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': GRID_SIZE_CANVAS_TEXT, 'column_span': None
}
CATEGORY_TYPE_RADIO_FRAME_COORDS = {'row': 9, 'column': 1}
NEW_CATEGORY_INPUT_COORDS = {'row': 8, 'column': 1}
NEW_CATEGORY_CANVAS_KWARGS = {
    'row': 8, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': NEW_CATEGORY_CANVAS_TEXT, 'column_span': None
}

MAIN_CANVAS_KWARGS = {
    'row': 1, 'column': 2, 'font_size': 24, 'padding_top': 8,
    'text': MAIN_CANVAS_TEXT, 'column_span': 10, 'bonus_width': 30
}

# tab control
DEFAULT_SEX = 'male'

REGISTRATION_BUTTON_SIZE = '7'
REGISTRATION_BUTTON_COORDS = {'row': 5, 'column': 1}

SEX_RADIO_FRAME_COORDS = {'row': 1, 'column': 1}

NICK_INPUT_COORDS = {'row': 0, 'column': 1}
NICKNAME_CANVAS_KWARGS = {
    'row': 0, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': NICKNAME_CANVAS_TEXT, 'column_span': 1
}

CREW_INPUT_COORDS = {'row': 2, 'column': 1}
CREW_CANVAS_KWARGS = {
    'row': 2, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': CREW_CANVAS_TEXT, 'column_span': 1
}

CITY_INPUT_COORDS = {'row': 3, 'column': 1}
CITY_CANVAS_KWARGS = {
    'row': 3, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': CITY_CANVAS_TEXT, 'column_span': 1
}
