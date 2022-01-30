from typing import Dict, List
from enum import Enum


class StrAlias(str, Enum):
    Y_AXIS = 'y_axis'
    X_AXIS = 'x_axis'


class IntAlias(int, Enum):
    X = 0
    Y = 1


def get_boys(grid_size: int) -> List[Dict[str, str]]:  # for test
    bboys = list()
    for index in range(1, grid_size + 1):
        bboys.append(
            {'name': f'boy{index}', 'crew': 'some crew', 'city': 'Cicity'}
        )
    return bboys
