import pytest
from constants import *
from fractal.scale_maker import generate_scale, generate_twelve_outputs

# Valid Inputs
EXPECTED_PATTERN = ["A","B","C","D","E","F","G","A"] 
EXPECTED_FROM_A = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'],
['D', 'E', 'F', 'G', 'A', 'B', 'C', 'D'],
 ['G', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
 ['F', 'G', 'A', 'B', 'C', 'D', 'E', 'F'],
 ['A#', 'C#', 'D#', 'F#', 'G#', 'A#'],
 ['D#', 'F#', 'G#', 'A#', 'C#', 'D#'],
 ['G#', 'A#', 'C#', 'D#', 'F#', 'G#'],
['C#', 'D#', 'F#', 'G#', 'A#', 'C#'],
 ['F#', 'G#', 'A#', 'C#', 'D#', 'F#'],
['B', 'C', 'D', 'E', 'F', 'G', 'A', 'B'],
 ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E']]
EXPECTED_FROM_C = [['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C'],
['F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb', 'F'],
['Bb', 'C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'],
['Ab', 'Bb', 'C', 'D', 'Eb', 'F', 'G', 'Ab'],
['Db', 'E', 'F#', 'A', 'B', 'C#'],
['Gb', 'A', 'B', 'C#', 'E', 'F#'],
['Cb', 'Db', 'E', 'F#', 'A', 'B'],
['Fb', 'Gb', 'A', 'B', 'C#', 'E'],
['A', 'B', 'C#', 'E', 'F#', 'A'],
['D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'],
['G', 'Ab', 'Bb', 'C', 'D', 'Eb', 'F', 'G']]
STARTING_LETTER = "A"
STARTING_LETTER2 = "C"
STARTING_LETTER3 = "E#"

# Invalid inputs
WRONG_PATTERN = "Not-a-pattern"
WRONG_STARTING_NOTE = 123


def test_generate_scale_happy_path():
    result = generate_scale(TWO_DOTS, STARTING_LETTER)
    assert EXPECTED_PATTERN == result

def test_generate_scale_invalid_pattern():
    with pytest.raises(Exception):
        generate_scale(WRONG_PATTERN, STARTING_LETTER)

def test_generate_scale_invalid_starting_note():
    with pytest.raises(Exception):
        generate_scale(EXPECTED_PATTERN, WRONG_STARTING_NOTE)

def test_generate_valid_sequence_from_A():
    result = generate_twelve_outputs(UNDERLYING_STRUTURE, DYNAMIC_CIRCULAR, STARTING_LETTER)
    for scale in range(12):
        assert EXPECTED_FROM_A[scale] == result[scale]

def test_generate_valid_sequence_from_C():
    result2 = generate_twelve_outputs(UNDERLYING_STRUTURE, DYNAMIC_CIRCULAR, STARTING_LETTER2)
    for scale in range(12):
        assert EXPECTED_FROM_C[scale] == result2[scale]

def test_generate_invalid_sequence_from_Esharp():
    with pytest.raises(Exception):
        generate_scale(WRONG_PATTERN, STARTING_LETTER3)

