from tkinter import Button, messagebox, Frame, Toplevel

from app.ui.handlers import (
    save_category_participants, remove_old_saves_if_exist
)
from app.ui.widgets.common import create_empty_strings
from app.ui.widgets.events import bind_esc_for_close
from app.ui.widgets.inputs import get_input
from app.ui.widgets.labels import change_text_canvas, get_canvas
from settings.ui.buttons import (
    CREATE_NEW_EVENT_BUTTON_TITLE, BUTTON_TEXT_COLOR,
    CREATE_NEW_EVENT_NAME_BUTTON_COORDS, CREATE_NEW_EVENT_BUTTON_SIZE,
    RENAME_EVENT_BUTTON_TEXT, RENAME_EVENT_BUTTON_SIZE,
    RENAME_EVENT_BUTTON_COORDS,
    SAVE_NEW_EVENT_TITLE_BUTTON_TITLE, SAVE_NEW_EVENT_TITLE_BUTTON_SIZE,
    SAVE_NEW_EVENT_TITLE_BUTTON_COORDS,
    SAVE_NEW_CATEGORY_GRID_SIZE_BUTTON_TEXT,
    SAVE_NEW_CATEGORY_GRID_SIZE_BUTTON_SIZE,
    SAVE_NEW_CATEGORY_GRID_SIZE_BUTTON_COORDS
)
from settings.ui.const import EMPTY_EVENT_INPUT_CANVAS_KWARGS, \
    NEW_EVENT_TITLE_INPUT_COORDS


def clicked_create_new_event(cls) -> None:
    if messagebox.askyesno(
        message="Create new event and close current window?"
    ):
        cls._window.destroy()
        cls.__init__()
    else:
        cls._window.focus_force()


def clicked_save_new_event_title(cls) -> None:
    new_event_name = cls._new_event_title_input.get()

    if new_event_name:
        if messagebox.askyesno(
            message=f"Change '{cls._event_name}' for '{new_event_name}'?"
        ):
            remove_old_saves_if_exist(event_name=cls._event_name)

            cls._event_name = new_event_name

            change_text_canvas(
                canvas=cls._event_name_title, text=cls._event_name
            )

            save_category_participants(cls=cls)
        cls._rename_window.destroy()
    else:
        get_canvas(
            window=cls._rename_window, **EMPTY_EVENT_INPUT_CANVAS_KWARGS
        )


def create_save_new_event_title_button(cls, frame: Toplevel) -> None:
    button = Button(
        master=frame, text=SAVE_NEW_EVENT_TITLE_BUTTON_TITLE,
        width=SAVE_NEW_EVENT_TITLE_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_save_new_event_title(cls=cls)
    )
    button.grid(**SAVE_NEW_EVENT_TITLE_BUTTON_COORDS)


def clicked_open_rename_event_frame(cls) -> None:
    cls._rename_window = Toplevel(master=cls._window)
    cls._rename_window.title(string='rename event')
    cls._rename_window.resizable(False, False)

    bind_esc_for_close(
        cls=cls, frame=cls._rename_window, window_title='_rename_window'
    )

    create_empty_strings(window=cls._rename_window, rows=[1])

    cls._new_event_title_input = get_input(
        window=cls._rename_window, **NEW_EVENT_TITLE_INPUT_COORDS
    )
    create_save_new_event_title_button(
        cls=cls, frame=cls._rename_window
    )

    cls._rename_window.transient(master=cls._window)
    cls._rename_window.grab_set()
    cls._window.wait_window(window=cls._rename_window)


def create_make_new_event_button(cls, frame: Frame) -> None:
    button = Button(
        master=frame, text=CREATE_NEW_EVENT_BUTTON_TITLE,
        width=CREATE_NEW_EVENT_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_create_new_event(cls=cls)
    )
    button.grid(**CREATE_NEW_EVENT_NAME_BUTTON_COORDS)


def create_rename_event_button(cls, frame: Frame) -> None:
    button = Button(
        master=frame, text=RENAME_EVENT_BUTTON_TEXT,
        width=RENAME_EVENT_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: clicked_open_rename_event_frame(cls=cls)
    )
    button.grid(**RENAME_EVENT_BUTTON_COORDS)


def save_new_category_grid_size(cls, frame: Toplevel, category: str) -> None:
    selected_grid_size = cls._selected_grid_size.get()
    print('selected', selected_grid_size)
    print('category', cls._categories[category])
    # TODO: save new selected grid and after ask message and close frame


def create_save_new_category_grid_size_button(
    cls, frame: Toplevel, category: str
) -> None:
    button = Button(
        master=frame, text=SAVE_NEW_CATEGORY_GRID_SIZE_BUTTON_TEXT,
        width=SAVE_NEW_CATEGORY_GRID_SIZE_BUTTON_SIZE, fg=BUTTON_TEXT_COLOR,
        command=lambda: save_new_category_grid_size(
            cls=cls, frame=frame, category=category
        )
    )
    button.grid(**SAVE_NEW_CATEGORY_GRID_SIZE_BUTTON_COORDS)
