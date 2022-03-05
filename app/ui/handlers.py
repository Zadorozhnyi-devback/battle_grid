from typing import List


def get_participant_fields(tab_type: str) -> List[str]:
    fields = ['crew', 'city']
    fields.append('nick') if tab_type == 'single' else ...
    return fields


def clean_participant_inputs(cls, inputs: List[str]) -> None:
    for my_input in inputs:
        getattr(cls, f'_{my_input}').delete(0, 'end')
