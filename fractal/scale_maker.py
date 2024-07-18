from constants import *
from fractal.maker_utils import set_starting_index, _move_index, rest_code, is_valid_input


def generate_scale(interval_pattern: list[int], starting_note: str) -> list:
    """
    Given an interval pattern and a starting note, generate the scale.
    """
    # keep track of the current index at each step
    current_index = 0
    result = []

    current_index = set_starting_index(starting_note, current_index, result) 
    moved_scale = _move_index(interval_pattern, current_index, result) 
    result = rest_code(interval_pattern, moved_scale)

    return result

def generate_twelve_outputs(UNDERLYING_STRUTURE: list[list], DYNAMIC_CIRCULAR: list, starting_note: str) -> list:
    """
        Generate a scale for each of the twelve notes of the dynamic circular input.
        Args: needs a starting note out of the twelve given in str
    """
    if is_valid_input(TWO_DOTS, starting_note):
        if not starting_note in DYNAMIC_CIRCULAR:
            raise Exception("Starting note must come from a list DYNAMIC_CIRCULAR")
        current_note_index = 0
        result = []
        for note in DYNAMIC_CIRCULAR:
            if note != starting_note:
                current_note_index += 1
            else:
                break
        for pattern in range(12):
            if current_note_index > 11:
                current_note_index -= 12
            result.append(generate_scale(UNDERLYING_STRUTURE[pattern], DYNAMIC_CIRCULAR[current_note_index]))
            current_note_index += 1
        
    return result

