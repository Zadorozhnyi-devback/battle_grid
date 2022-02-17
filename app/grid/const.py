from typing import Dict, List
from enum import Enum


class StrAlias(str, Enum):
    Y_AXIS = 'y_axis'
    X_AXIS = 'x_axis'


class IntAlias(int, Enum):
    X = 0
    PATH = 0
    FIRST = 0
    Y = 1
    SIZE = 1
    CURRENT_ICON = -1


def get_boys(grid_size: int) -> List[Dict[str, str]]:  # for test
    bboys = list()
    for index in range(1, grid_size + 1):
        bboys.append(
            {
                'name': f'girl{index}',
                'city': 'Cicity',
                'crew': 'Ruffneck Attack'
            }
        )
    return bboys
