# canvases, labels
CURRENT_PATH = 'load folder'
MAIN_CANVAS_TEXT = 'welcome to battle grid!'
EVENT_NAME_CANVAS_TEXT = 'event name:'
NICKNAME_CANVAS_TEXT = 'nick:'
CITY_CANVAS_TEXT = 'city:'
NEW_CATEGORY_CANVAS_TEXT = 'category:'
CREW_CANVAS_TEXT = 'crew:'
GRID_SIZE_CANVAS_TEXT = 'grid:'

# buttons
DESTINATION_BUTTON_TITLE = 'choose folder'
SAVE_EVENT_NAME_BUTTON_TITLE = 'save'
CREATE_NEW_EVENT_BUTTON_TITLE = 'create new'
OPEN_EVENT_BUTTON_TEXT = 'open'
REGISTER_BUTTON_TITLE = 'register'
UNREGISTER_BUTTON_TITLE = 'unregister'
ADD_TAB_BUTTON_TEXT = 'add category'
REMOVE_TAB_BUTTON_TEXT = 'remove category'


# errors


# settings
# common
DEFAULT_DOWNLOAD_PATH = 'output_grids'
WINDOW_TITLE = 'battle grid'
WINDOW_SIZE = '800x610'
TAB_CONTROL_WINDOW_SIZE = {'width': 746, 'height': 300}
MY_FONT = 'Arial Bold'
DEFAULT_FONT_SIZE = 14
BUTTON_TEXT_COLOR = 'red'

# main window
DEFAULT_GRID_SIZE = '8'
DEFAULT_CATEGORY_TYPE = 'single'

MAIN_CANVAS_KWARGS = {
    'row': 1, 'column': 2, 'font_size': 24, 'padding_top': 8,
    'text': MAIN_CANVAS_TEXT, 'column_span': 20, 'bonus_width': 50
}

DESTINATION_BUTTON_SIZE = '12'
CURR_PATH_LABEL_COORDS = {'row': 4, 'column': 0}
DESTINATION_BUTTON_COORDS = {'row': 5, 'column': 1}

EVENT_NAME_CANVAS_KWARGS = {
    'row': 7, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': EVENT_NAME_CANVAS_TEXT, 'column_span': None
}
EVENT_NAME_TITLE_CANVAS_KWARGS = {
    'row': 7, 'column': 1, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'column_span': None
}
EVENT_NAME_INPUT_COORDS = {'row': 7, 'column': 1}

SAVE_EVENT_NAME_BUTTON_SIZE = '7'
SAVE_EVENT_NAME_BUTTON_COORDS = {'row': 7, 'column': 2}

CREATE_NEW_EVENT_BUTTON_SIZE = '9'
CREATE_NEW_EVENT_NAME_BUTTON_COORDS = {'row': 7, 'column': 2}

OPEN_EVENT_BUTTON_SIZE = '8'
OPEN_EVENT_BUTTON_COORDS = {'row': 7, 'column': 3}

GRID_SIZE_RADIO_FRAME_COORDS = {'row': 8, 'column': 1}
GRID_SIZE_CANVAS_KWARGS = {
    'row': 8, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': GRID_SIZE_CANVAS_TEXT, 'column_span': None
}

ADD_TAB_BUTTON_SIZE = '10'
ADD_TAB_BUTTON_COORDS = {'row': 9, 'column': 2}
REMOVE_TAB_BUTTON_SIZE = '12'
REMOVE_TAB_BUTTON_COORDS = {'row': 9, 'column': 3}

NEW_CATEGORY_INPUT_COORDS = {'row': 9, 'column': 1}
NEW_CATEGORY_CANVAS_KWARGS = {
    'row': 9, 'column': 0, 'font_size': DEFAULT_FONT_SIZE, 'padding_top': 5,
    'text': NEW_CATEGORY_CANVAS_TEXT, 'column_span': None
}
CATEGORY_TYPE_RADIO_FRAME_COORDS = {'row': 10, 'column': 1}

# tab control
DEFAULT_SEX = 'male'

REGISTER_BUTTON_SIZE = '7'
UNREGISTER_BUTTON_SIZE = '8'
REGISTER_BUTTON_COORDS = {'row': 5, 'column': 1}
UNREGISTER_BUTTON_COORDS = {'row': 6, 'column': 1}

SEX_RADIO_FRAME_COORDS = {'row': 1, 'column': 1}

NICK_INPUT_COORDS = {'row': 0, 'column': 1}
NICK_CANVAS_KWARGS = {
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
