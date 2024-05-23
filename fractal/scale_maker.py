from constants import NOTE_INDEXES, SHARP_FLAT_EQUALITY_LIST


def generate_scale(interval_pattern, starting_note) -> list:
    """
    Given an interval pattern and a starting note, generate the scale.
    1 = half step, 2 = whole step, 3 = one and a half steps, etc.
    """
    # keep track of the current index at each step
    current_index = 0
    generated_notes = []

    for note in NOTE_INDEXES:
        if NOTE_INDEXES[note] == starting_note:
            current_index = note
            generated_notes.append(starting_note)

        # find the maximum index to find the period of circulation
        maximum_index = 0
        if note > maximum_index:
            maximum_index = note
    
    for i in interval_pattern:
        current_index += i
        if current_index > maximum_index:
            current_index -= (maximum_index + 1)
        generated_notes.append(NOTE_INDEXES[current_index])
    
    # replace same position
    for i in range(len(generated_notes)):
        for j in range(len(generated_notes)-1):
            if generated_notes[i] != generated_notes[j] and generated_notes[i][0] == generated_notes[j][0]:
                for note in SHARP_FLAT_EQUALITY_LIST:
                    if note == generated_notes[j]:
                        duplicate_index = SHARP_FLAT_EQUALITY_LIST[note]
                for note in SHARP_FLAT_EQUALITY_LIST:
                    if duplicate_index == SHARP_FLAT_EQUALITY_LIST[note] and  note != generated_notes[j]:
                        generated_notes[j] = note


    return generated_notes

