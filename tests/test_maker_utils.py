

import pytest
from fractal.maker_utils import is_valid_input, set_starting_index


def test_interval_pattern_with_more_than_5_elements():
    # TODO: This actually shows it is not working as expected!!!
    interval_pattern = [1, 2, 3, 4, 5, 6]
    starting_note = "C"
    with pytest.raises(Exception):
        is_valid_input(interval_pattern, starting_note)

def test_starting_note_more_than_two_chars():
    # TODO: This actually shows it is not working as expected!!!
    interval_pattern = [1, 2, 3, 4, 5]
    starting_note = "ABC" # Should not work
    with pytest.raises(Exception):
        is_valid_input(interval_pattern, starting_note)

# starting_note is not in NOTE_INDEXES
def test_starting_note():
    ...