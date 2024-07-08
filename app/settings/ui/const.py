# canvases, labels, inputs
from pathlib import Path
from tkinter import VERTICAL

CURRENT_PATH = 'load folder'
MAIN_CANVAS_TEXT = 'welcome to battle grid!'
EVENT_NAME_CANVAS_TEXT = 'event name:'
NICKNAME_CANVAS_TEXT = 'nick:'
CITY_CANVAS_TEXT = 'city:'
CATEGORY_CANVAS_TEXT = 'category:'
CREW_CANVAS_TEXT = 'crew:'
GRID_SIZE_CANVAS_TEXT = 'grid:'
EMPTY_EVENT_INPUT_CANVAS_TEXT = 'empty event name'
SAME_EVENT_NAME_CANVAS_TEXT = 'same event title'
EVENT_NAME_IS_TOO_LONG_TEXT = 'event name is too long'


# errors


# settings

# defaults
DEFAULT_GRID_SIZE = '8'
DEFAULT_CATEGORY_TYPE = 'single'
DEFAULT_DOWNLOAD_PATH = str(Path('output_grids').resolve())
DEFAULT_FONT_SIZE = 14

# common
MAIN_WINDOW_TITLE = 'battle grid'
MAIN_WINDOW_SIZE = '800x610'
TAB_CONTROL_WINDOW_SIZE = {'width': 746, 'height': 300}

# temporary
TEMP_INPUT_COORDS = {'column': 0, 'row': 0, 'sticky': None}

# fonts
ARIAL_BOLD = 'Arial Bold'
HELVETICA = 'Helvetica'

# main window
MAIN_CANVAS_KWARGS = {
    'row': 1, 'column': 0,
    'font_size': 24,
    'padding_y': 10,
    'x_move_to': '250',
    'text': MAIN_CANVAS_TEXT,
    'column_span': 2,
    'bonus_width': 500,
    'sticky': None
}

CURR_PATH_LABEL_COORDS = {
    'row': 4, 'column': 0, 'sticky': 'W', 'columnspan': 100,
    'padx': (4, 4), 'pady': (4, 4)
}

EVENT_NAME_CANVAS_KWARGS = {
    'row': 0, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_y': 10,
    'text': EVENT_NAME_CANVAS_TEXT, 'column_span': None, 'sticky': 'W'
}
EVENT_NAME_INPUT_COORDS = {'row': 0, 'column': 1, 'sticky': 'W'}  # +

# tab control
TAB_CONTROL_WINDOW_COORDS = {
    'column': 0, 'row': 11, 'columnspan': 40, 'sticky': 'W'
}

SCROLLBAR_KWARGS = {
    'column': 6, 'row': 0, 'rowspan': 100, 'pady': (4, 4), 'sticky': 'ens'
}
TEXT_WINDOW_KWARGS = {
    'column': 5, 'row': 0, 'rowspan': 100, 'sticky': 'E', 'pady': (4, 4)
}

TAB_LEFT_SEPARATOR_KWARGS = {
    'orient': VERTICAL, 'column': 1, 'row': 0, 'row_span': 100,
    'sticky': 'wns', 'pad_y': (6, 6), 'pad_x': (4, 4)
}
TAB_RIGHT_SEPARATOR_KWARGS = {
    'orient': VERTICAL, 'column': 3, 'row': 0, 'row_span': 100,
    'sticky': 'ens', 'pad_y': (6, 6), 'pad_x': (0, 4)
}

# registration frame
REGISTRATION_FRAME_COORDS = {'row': 0, 'column': 0, 'sticky': 'wn', 'pady': 5}

DEFAULT_SEX = 'male'

SEX_RADIO_FRAME_COORDS = {'row': 1, 'column': 1}

NICK_INPUT_COORDS = {'row': 0, 'column': 1, 'sticky': 'W'}
NICK_CANVAS_KWARGS = {
    'row': 0, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_y': 5,
    'text': NICKNAME_CANVAS_TEXT, 'column_span': None, 'sticky': 'W'
}

CREW_INPUT_COORDS = {'row': 2, 'column': 1, 'sticky': 'W'}
CREW_CANVAS_KWARGS = {
    'row': 2, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_y': 5,
    'text': CREW_CANVAS_TEXT, 'column_span': None, 'sticky': 'W'
}

CITY_INPUT_COORDS = {'row': 3, 'column': 1, 'sticky': 'W'}
CITY_CANVAS_KWARGS = {
    'row': 3, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_y': 5,
    'text': CITY_CANVAS_TEXT, 'column_span': None, 'sticky': 'W'
}

# category info frame
CATEGORY_INFO_FRAME_COORDS = {
    'row': 0, 'column': 2, 'sticky': 'wn', 'pady': 5, 'columnspan': None
}

EVENT_NAME_TITLE_CANVAS_KWARGS = {
    'row': 0, 'column': 0, 'font_size': DEFAULT_FONT_SIZE,
    'padding_y': 5, 'column_span': None, 'sticky': 'W', 'bonus_width': 50
}

SELECTED_GRID_CANVAS_KWARGS = {
    'row': 1, 'column': 0, 'font_size': DEFAULT_FONT_SIZE,
    'padding_y': 5, 'column_span': None, 'sticky': 'W', 'bonus_width': 50
}

SELECTED_CATEGORY_TYPE_CANVAS_KWARGS = {
    'row': 2, 'column': 0, 'font_size': DEFAULT_FONT_SIZE,
    'padding_y': 5, 'column_span': None, 'sticky': 'W', 'bonus_width': 40
}

MALE_AND_FEMALE_CANVAS_KWARGS = {
    'row': 3, 'column': 0, 'font_size': DEFAULT_FONT_SIZE,
    'padding_y': 5, 'column_span': None, 'sticky': 'W'
}

# additional windows
# change event name
NEW_EVENT_TITLE_INPUT_COORDS = {'row': 0, 'column': 0, 'sticky': 'W'}

EVENT_INPUT_CANVAS_KWARGS = {
    'row': 1, 'column': 0, 'font_size': 13, 'padding_y': 1,
    'column_span': None, 'sticky': None
}


# category toplevel frame
CATEGORY_TITLE_INPUT_COORDS = {'row': 0, 'column': 1, 'sticky': 'W'}
CATEGORY_CANVAS_KWARGS = {
    'row': 0, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_y': 10,
    'text': CATEGORY_CANVAS_TEXT, 'column_span': None, 'sticky': 'W'
}
CATEGORY_TYPE_RADIO_FRAME_COORDS = {'row': 1, 'column': 1}

GRID_SIZE_RADIO_FRAME_COORDS = {'row': 3, 'column': 1, 'sticky': 'W'}
GRID_SIZE_CANVAS_KWARGS = {
    'row': 3, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_y': 10,
    'text': GRID_SIZE_CANVAS_TEXT, 'column_span': None, 'sticky': 'W'
}
