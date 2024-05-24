import pytest
from constants import PATTERN_RED
from fractal.scale_maker import generate_scale

# Valid Inputs
EXPECTED_PATTERN = ["A","B","C","D","E","F","G","A"] 
STARTING_LETTER = "A"

# Invalid inputs
WRONG_PATTERN = "Not-a-pattern"
WRONG_STARTING_NOTE = 123


def test_generate_scale_happy_path():
    result = generate_scale(PATTERN_RED, STARTING_LETTER)
    assert EXPECTED_PATTERN == result

def test_generate_scale_invalid_pattern():
    with pytest.raises(Exception):
        generate_scale(WRONG_PATTERN, STARTING_LETTER)

def test_generate_scale_invalid_starting_note():
    with pytest.raises(Exception):
        generate_scale(EXPECTED_PATTERN, WRONG_STARTING_NOTE)