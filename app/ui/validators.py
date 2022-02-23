from app.ui.widgets.labels import change_text_canvas


def validate_category_existing(cls) -> bool:
    print(cls._categories)
    if not cls._category_input.get() in cls._categories.keys():
        change_text_canvas(canvas=cls._main_canvas, text='added new tab')
        return True
    else:
        change_text_canvas(canvas=cls._main_canvas, text='category exists')


def validate_input_length(cls, tab_type: str) -> bool:
    entries = ['crew', 'city']
    if tab_type == 'single':
        entries.append('nick')
    max_length = 16 if cls._selected_grid_size.get() in (8, 16) else 21
    for entry in entries:
        if len(getattr(cls, f'_{entry}').get()) > max_length:
            change_text_canvas(
                canvas=cls._main_canvas, text=f'{entry} input is too long'
            )
            return False
    return True
