from constants import NOTE_INDEXES, SHARP_FLAT_EQUALITY_LIST


def is_valid_input(interval_pattern, starting_note):
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

def generate_scale(interval_pattern, starting_note) -> list:
    """
    Given an interval pattern and a starting note, generate the scale.
    1 = half step, 2 = whole step, 3 = one and a half steps, etc.
    """
    # keep track of the current index at each step
    current_index = 0
    result = []

    if is_valid_input(interval_pattern, starting_note):
        for note in NOTE_INDEXES:
            if NOTE_INDEXES[note] == starting_note:
                current_index = note
                result.append(starting_note)

            # find the maximum index to find the period of circulation
            maximum_index = 0
            if note > maximum_index:
                maximum_index = note
        
        for i in interval_pattern:
            current_index += i
            if current_index > maximum_index:
                current_index -= (maximum_index + 1)
            result.append(NOTE_INDEXES[current_index])
        
        # replace same position
        for i in range(len(result)):
            for j in range(len(result)-1):
                if result[i] != result[j] and result[i][0] == result[j][0]:
                    for note in SHARP_FLAT_EQUALITY_LIST:
                        if note == result[j]:
                            duplicate_index = SHARP_FLAT_EQUALITY_LIST[note]
                    for note in SHARP_FLAT_EQUALITY_LIST:
                        if duplicate_index == SHARP_FLAT_EQUALITY_LIST[note] and  note != result[j]:
                            result[j] = note

    return result

        

