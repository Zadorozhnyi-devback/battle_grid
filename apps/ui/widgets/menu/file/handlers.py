from app.settings.ui.toplevel import EVENT_TOPLEVEL_FIELDS
from apps.ui.handlers.cleaners import destroy_if_exists
from apps.ui.validators import validate_event_name_input
from apps.ui.widgets.labels.handlers import change_text_canvas
from apps.ui.widgets.menu.file.event.rename import create_rename_event_toplevel
from apps.ui.widgets.menu.handlers import enable_menu


__all__ = (
    'save_event_name',
)


def save_event_name(self) -> None:
    if validate_event_name_input(self) is True:
        self._event_name = self._event_name_input.get()

        self._file_menu.add_command(
            label='Rename event',
            command=lambda: create_rename_event_toplevel(self)
        )

        enable_menu(self, menu='Category')

        destroy_if_exists(self, fields=EVENT_TOPLEVEL_FIELDS)

        change_text_canvas(
            canvas=self._main_canvas,
            text=f"event {self._event_name!r} was created"
        )
