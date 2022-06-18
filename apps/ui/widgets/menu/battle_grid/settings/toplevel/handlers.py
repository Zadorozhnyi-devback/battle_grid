import getpass
from pathlib import Path
from tkinter import filedialog

from app.settings.ui.const import CURRENT_PATH


__all__ = (
    'clicked_choose_dir',
)


def clicked_choose_dir(self) -> None:
    directory = filedialog.askdirectory(
        # gonna work on mac, have to check for windows and linux
        # initialdir=os.path.normpath("C://") try on Windows
        parent=self._settings_toplevel,
        initialdir=f'/Users/{getpass.getuser()}/'
    )
    if directory is not None:
        self._destination_path = str(Path(directory).resolve())
    path = self._destination_path.split('/')[-1]
    self._curr_path_label.configure(text=f'{CURRENT_PATH}: {path}')
