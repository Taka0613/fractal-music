from constants import NOTE_INDEXES, SHARP_FLAT_EQUALITY


def is_valid_input(interval_pattern: list[int], starting_note: str) -> bool:
    """Check the pattern is a list of integers, no smaller than 5 digits
    and each digit must be positive and no bigger than 4
    
    and that starting note is always ONE-LETTER and two-chars len() 
    and it is only one of the notes c,e,d,f,g,a,b"""

    result = True

    if not isinstance(interval_pattern, list) or len(interval_pattern) < 5 or len(interval_pattern) > 7:
        raise Exception("Interval pattern must be a list of 5 to 7 elements")

    elif not all([isinstance(note, int) for note in interval_pattern]) or not all(1 <= note <= 4 for note in interval_pattern):
        raise Exception("Interval pattern must be a list of integers from 1 to 4")  
    
    elif not isinstance(starting_note, str) or not starting_note in SHARP_FLAT_EQUALITY:
        raise Exception("Starting note must be a valid chaeracter")
    
    return result

def _set_starting_index(starting_note: str, current_index: int, output_scale: list) -> int:
    if starting_note == 'C':
        output_scale.append('C')
        current_index = 0
    elif starting_note == 'F':
        current_index = 5
        output_scale.append('F')
    for note in NOTE_INDEXES:
        if NOTE_INDEXES[note] == starting_note:
            current_index = note
            output_scale.append(starting_note)
    return current_index
    
    
def _move_index(interval_pattern: list[int], current_index: int, output_scale: list) -> list:
    # The period of circulation is always 12
    maximum_index = 11
    for index in interval_pattern:
        current_index += index
        if current_index > maximum_index:
            current_index -= (maximum_index + 1)
        output_scale.append(NOTE_INDEXES[current_index])
    return output_scale



def _change_same_letter(interval_pattern: list[int], output_scale: list) -> list:
        """    
        1 = half step, 2 = whole step, 3 = one and a half steps, etc.
        """
        temp_scale = []
        for index in range(len(output_scale)):
            # when a note has no equivalent note
            if output_scale[index] == 'D' or output_scale[index] == 'G' or output_scale[index] == 'A':
                fixed_index = index
                temp_scale = output_scale[fixed_index:] + output_scale[:fixed_index]
                break

        # when an output_scale includes D, G or A
        if temp_scale != []:
            for pos in range(len(temp_scale)-1):
                # when we compare the first and the last note in original output_scale
                # they should be exactly same note

                # when an interval pattern is non-star
                if pos != 0 and pos == 7-index and len(temp_scale) == 8:
                    temp_scale[pos+1] = temp_scale[pos]
                elif temp_scale[pos][0] == temp_scale[pos+1][0] or (temp_scale[pos] == "Cb" and temp_scale[pos+1] == "B#"):
                    for note in SHARP_FLAT_EQUALITY:
                        if note == temp_scale[pos+1]:
                            duplicate_index = SHARP_FLAT_EQUALITY[note]
                    for note in SHARP_FLAT_EQUALITY:
                        if duplicate_index == SHARP_FLAT_EQUALITY[note] and  note != temp_scale[pos+1]:
                            temp_scale[pos+1] = note
        # restore a original output_scale from new output_scale
            # if an interval pattern is non-star
            if len(interval_pattern) == 7:
                output_scale = temp_scale[8-fixed_index:] + temp_scale[:8-fixed_index]
            # if an interval pattern is star
            elif len(interval_pattern) == 5:
                output_scale = temp_scale[6-fixed_index:] + temp_scale[:6-fixed_index]

        # when an output_scale does not D, G or A
        else:
            for pos in range(len(output_scale)-1):
                if output_scale[pos][0] == output_scale[pos+1][0]  or (output_scale[pos] == "Cb" and output_scale[pos+1] == "B#"):
                    for note1 in SHARP_FLAT_EQUALITY:
                        current_note_index = SHARP_FLAT_EQUALITY[output_scale[pos + 1]]
                    for note, index in SHARP_FLAT_EQUALITY.items():
                        if index == current_note_index and note != output_scale[pos + 1]:
                            output_scale[pos + 1] = note
                            break
            output_scale[-1] = output_scale[0]

        return output_scale