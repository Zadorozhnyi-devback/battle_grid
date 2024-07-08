import getpass
import json
from tkinter import filedialog

from app.settings.ui.const import EVENT_NAME_INPUT_COORDS
from app.settings.ui.fields.category_toplevel import CATEGORY_TOPLEVEL_FIELDS
from app.settings.ui.fields.event_toplevel import EVENT_TOPLEVEL_FIELDS
from apps.ui.const import BEGINNING
from apps.ui.handlers.cleaners import destroy_if_exists, remove_old_categories
from apps.ui.widgets.inputs import get_input
from apps.ui.widgets.labels.handlers import change_text_canvas
from apps.ui.widgets.menu.file.handlers import save_event_name
from apps.ui.widgets.tab_control.windows.creators import (
    create_loaded_categories
)


__all__ = (
    'open_event',
)


def open_event(self) -> None:
    destroy_if_exists(
        self,
        fields=[*EVENT_TOPLEVEL_FIELDS, *CATEGORY_TOPLEVEL_FIELDS]
    )

    event_json = filedialog.askopenfilename(
        parent=self._window,
        initialdir=(
            f'/Users/{getpass.getuser()}/PycharmProjects/battle_grid/events/'
        )
    )
    if event_json:
        destroy_if_exists(self, fields=['_event_name_title'])
        self._event_name_input = get_input(
            frame=self._window,
            **EVENT_NAME_INPUT_COORDS
        )

        event_name = event_json.split('/')[-1].split('_')[0]
        self._event_name_input.insert(BEGINNING, event_name)

        save_event_name(self)
        change_text_canvas(
            canvas=self._main_canvas,
            text=f"event {event_name!r} was loaded"
        )

        with open(file=event_json, encoding='utf-8') as event_file:
            file_data = json.load(event_file)

        remove_old_categories(self)
        create_loaded_categories(self, json_data=file_data)
