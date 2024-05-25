import pytest
from constants import *
from fractal.scale_maker import generate_scale, generate_twelve_outputs

# Valid Inputs
EXPECTED_PATTERN = ["A","B","C","D","E","F","G","A"] 
STARTING_LETTER = "A"

# Invalid inputs
WRONG_PATTERN = "Not-a-pattern"
WRONG_STARTING_NOTE = 123


def test_generate_scale_happy_path():
    result = generate_scale(PATTERN_TWO_DOTS, STARTING_LETTER)
    assert EXPECTED_PATTERN == result

def test_generate_scale_invalid_pattern():
    with pytest.raises(Exception):
        generate_scale(WRONG_PATTERN, STARTING_LETTER)

def test_generate_scale_invalid_starting_note():
    with pytest.raises(Exception):
        generate_scale(EXPECTED_PATTERN, WRONG_STARTING_NOTE)

def test_generate_valid_sequence():
    result = generate_twelve_outputs(UNDERLYING_STRUTURE, DYNAMIC_CIRCULAR, STARTING_LETTER)
    assert EXPECTED_PATTERN == result[0]
    