from constants import *

def is_valid_input(interval_pattern: list[int], starting_note: str) -> bool:
    """Check the pattern is a list of integers, no smaller than 5 digits
    and each digit must be positive and no bigger than 4
    
    and that starting note is always ONE-LETTER and two-chars len() 
    and it is only one of the notes c,e,d,f,g,a,b"""

    result = True

    if not isinstance(interval_pattern, list) or len(interval_pattern) <= 5:
        if not all([isinstance(note, int) for note in interval_pattern]):
            raise Exception("Interval pattern must be a list of integers")  
    
    if not isinstance(starting_note, str) and starting_note in NOTE_INDEXES.items():
        raise Exception("Starting note must be a string")
    
    return result

def generate_scale(interval_pattern: list[int], starting_note: str) -> list:
    """
    Given an interval pattern and a starting note, generate the scale.
    1 = half step, 2 = whole step, 3 = one and a half steps, etc.
    """
    # keep track of the current index at each step
    current_index = 0
    result = []

    if is_valid_input(interval_pattern, starting_note):
        #deal with exceptions first
        if starting_note == 'C':
            result.append('C')
            current_index = 0
        elif starting_note == 'F':
            current_index = 5
            result.append('F')
        for note in NOTE_INDEXES:
            if NOTE_INDEXES[note] == starting_note:
                current_index = note
                result.append(starting_note)

            # The period of circulation is always 12
            maximum_index = 11
        
        for index in interval_pattern:
            current_index += index
            if current_index > maximum_index:
                current_index -= (maximum_index + 1)
            result.append(NOTE_INDEXES[current_index])
        
        new_result = []
        for index in range(len(result)):
            # when a note has no equivalent note
            if result[index] == 'D' or result[index] == 'G' or result[index] == 'A':
                fixed_index = index
                new_result = result[fixed_index:] + result[:fixed_index]
                break

        if new_result != []:
            for pos in range(len(new_result)-1):
                # when we compare the first and the last note in original result
                # they should be exactly same note
                if pos == 7-index and len(new_result) == 8:
                    new_result[pos+1] = new_result[pos]
                elif new_result[pos][0] == new_result[pos+1][0] or (new_result[pos] == "Cb" and new_result[pos+1] == "B#"):
                    for note in SHARP_FLAT_EQUALITY:
                        if note == new_result[pos+1]:
                            duplicate_index = SHARP_FLAT_EQUALITY[note]
                    for note in SHARP_FLAT_EQUALITY:
                        if duplicate_index == SHARP_FLAT_EQUALITY[note] and  note != new_result[pos+1]:
                            new_result[pos+1] = note
        # restore a original result from new result
            if len(interval_pattern) == 7:
                result = new_result[8-fixed_index:] + new_result[:8-fixed_index]
            elif len(interval_pattern) == 5:
                result = new_result[6-fixed_index:] + new_result[:6-fixed_index]
        else:
            for pos in range(len(result)-1):
                if result[pos][0] == result[pos+1][0]  or (result[pos] == "Cb" and result[pos+1] == "B#"):
                    for note1 in SHARP_FLAT_EQUALITY:
                        current_note_index = SHARP_FLAT_EQUALITY[result[pos + 1]]
                    for note, index in SHARP_FLAT_EQUALITY.items():
                        if index == current_note_index and note != result[pos + 1]:
                            result[pos + 1] = note
                            break
            result[-1] = result[0]

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

