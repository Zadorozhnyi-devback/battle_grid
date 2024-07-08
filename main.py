import os

from apps.ui.tkin import BattleGridUI


if __name__ == '__main__':
    entry_point_path = os.path.dirname(os.path.realpath(__file__))
    BattleGridUI(entry_point_path=entry_point_path)
