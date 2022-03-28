# canvases, labels
from tkinter import VERTICAL

CURRENT_PATH = 'load folder'
MAIN_CANVAS_TEXT = 'welcome to battle grid!'
EVENT_NAME_CANVAS_TEXT = 'event name:'
NICKNAME_CANVAS_TEXT = 'nick:'
CITY_CANVAS_TEXT = 'city:'
NEW_CATEGORY_CANVAS_TEXT = 'category:'
CREW_CANVAS_TEXT = 'crew:'
GRID_SIZE_CANVAS_TEXT = 'grid:'
EMPTY_EVENT_INPUT_CANVAS_TEXT = 'empty event name'


# errors


# settings
# common
DEFAULT_DOWNLOAD_PATH = 'output_grids'
MAIN_WINDOW_TITLE = 'battle grid'
MAIN_WINDOW_SIZE = '800x610'
TAB_CONTROL_WINDOW_SIZE = {'width': 746, 'height': 300}
MY_FONT = 'Arial Bold'
DEFAULT_FONT_SIZE = 14

# main window
DEFAULT_GRID_SIZE = '8'
DEFAULT_CATEGORY_TYPE = 'single'

MAIN_CANVAS_KWARGS = {
    'row': 1, 'column': 2, 'font_size': 24, 'padding_top': 8,
    'text': MAIN_CANVAS_TEXT, 'column_span': 20, 'bonus_width': 200
}

CURR_PATH_LABEL_COORDS = {'row': 4, 'column': 0}

EVENT_NAME_CANVAS_KWARGS = {
    'row': 7, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': EVENT_NAME_CANVAS_TEXT, 'column_span': None
}
EVENT_NAME_TITLE_CANVAS_KWARGS = {
    'row': 7, 'column': 1, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'column_span': None
}
EVENT_NAME_INPUT_COORDS = {'row': 7, 'column': 1}

GRID_SIZE_RADIO_FRAME_COORDS = {'row': 8, 'column': 1, 'sticky': 'W'}
GRID_SIZE_CANVAS_KWARGS = {
    'row': 8, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': GRID_SIZE_CANVAS_TEXT, 'column_span': None
}

NEW_CATEGORY_INPUT_COORDS = {'row': 9, 'column': 1}
NEW_CATEGORY_CANVAS_KWARGS = {
    'row': 9, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': NEW_CATEGORY_CANVAS_TEXT, 'column_span': None
}
CATEGORY_TYPE_RADIO_FRAME_COORDS = {'row': 10, 'column': 1}

TAB_CONTROL_WINDOW_COORDS = {
    'column': 0, 'row': 14, 'columnspan': 40, 'sticky': 'W'
}

# tab control

TAB_LEFT_SEPARATOR_KWARGS = {
    'orient': VERTICAL, 'column': 1, 'row': 0, 'row_span': 100,
    'sticky': 'wns', 'pad_y': (6, 6), 'pad_x': (4, 4)
}
TAB_RIGHT_SEPARATOR_KWARGS = {
    'orient': VERTICAL, 'column': 3, 'row': 0, 'row_span': 100,
    'sticky': 'ens', 'pad_y': (6, 6), 'pad_x': (0, 4)
}

# registration frame
CREATE_REGISTRATION_FRAME_COORDS = {
    'row': 0, 'column': 0, 'sticky': 'wn', 'pady': 5
}

DEFAULT_SEX = 'male'

SEX_RADIO_FRAME_COORDS = {'row': 1, 'column': 1}

NICK_INPUT_COORDS = {'row': 0, 'column': 1}
NICK_CANVAS_KWARGS = {
    'row': 0, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': NICKNAME_CANVAS_TEXT, 'column_span': None
}

CREW_INPUT_COORDS = {'row': 2, 'column': 1}
CREW_CANVAS_KWARGS = {
    'row': 2, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': CREW_CANVAS_TEXT, 'column_span': None
}

CITY_INPUT_COORDS = {'row': 3, 'column': 1}
CITY_CANVAS_KWARGS = {
    'row': 3, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': CITY_CANVAS_TEXT, 'column_span': None
}

# info frame
CATEGORY_INFO_FRAME_COORDS = {'row': 0, 'column': 2, 'sticky': 'wn', 'pady': 5}

SELECTED_GRID_CANVAS_KWARGS = {
    'row': 0, 'column': 0, 'font_size': DEFAULT_FONT_SIZE,
    'padding_top': 5, 'column_span': None
}

# additional windows
# change event name
NEW_EVENT_TITLE_INPUT_COORDS = {'row': 0, 'column': 0}

EMPTY_EVENT_INPUT_CANVAS_KWARGS = {
    'row': 1, 'column': 0, 'font_size': 13, 'padding_top': 1,
    'text': EMPTY_EVENT_INPUT_CANVAS_TEXT, 'column_span': None, 'sticky': None
}


# change grid size
CHANGE_GRID_SIZE_RADIO_FRAME_COORDS = {'row': 0, 'column': 0, 'sticky': 'W'}
