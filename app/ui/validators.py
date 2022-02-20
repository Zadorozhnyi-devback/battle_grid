# from typing import List, Dict
#
#
# def get_field_max_length(grid_size: int) -> int:
#     if grid_size == 32:
#         return 40
#     elif grid_size == 16:
#         return 50
#     else:  # 8
#         return 60
#
#
# def validate_strings_length(people: List[Dict[str, str]], grid_size: int):
#     max_length = get_field_max_length(grid_size=grid_size)
#     for person in people:
#         for k, v in person.items():
#             if len(v) > max_length:
#                 return
from app.ui.widgets.labels import change_text_canvas


def validate_category_existing(cls) -> bool:
    if not cls._new_category.get() in cls._categories.keys():
        change_text_canvas(canvas=cls._main_canvas, text='added new tab')
        return True
    else:
        change_text_canvas(canvas=cls._main_canvas, text='category exists')
