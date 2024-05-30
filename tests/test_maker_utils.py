import pytest
from fractal.maker_utils import is_valid_input, _set_starting_index


def test_interval_pattern_with_more_than_7_elements():
    # TODO: This actually shows it is not working as expected!!!
    # solved
    interval_pattern = [1, 2, 3, 4, 1, 2, 3, 4]
    starting_note = "C"
    with pytest.raises(Exception):
        is_valid_input(interval_pattern, starting_note)

def test_interval_pattern_int():
    #interval pattern must be a list
    interval_pattern =  123412
    starting_note = "C"
    with pytest.raises(Exception):
        is_valid_input(interval_pattern, starting_note)

def test_interval_pattern_invalid_int():
    #interval pattern must be a list of integer from 1 to 4
    interval_pattern =  [1,2,3,4,5]
    starting_note = "C"
    with pytest.raises(Exception):
        is_valid_input(interval_pattern, starting_note)

def test_starting_note_more_than_two_chars():
    # TODO: This actually shows it is not working as expected!!!
    #solved
    interval_pattern = [1, 2, 3, 4, 1]
    starting_note = "ABCK" # Should not work
    with pytest.raises(Exception):
        is_valid_input(interval_pattern, starting_note)

# starting_note is not in SHARP_FLAT_EQUALITY <= Here I changed from NOTE_INDEX
def test_starting_note_invalid_char():
    interval_pattern =  [1,2,3,4,1]
    # starting note is not in SHARP_FLAT EQUALITY
    starting_note = "K"
    with pytest.raises(Exception):
        is_valid_input(interval_pattern, starting_note)