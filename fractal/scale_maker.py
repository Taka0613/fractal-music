from constants import NOTE_INDEXES, SHARP_FLAT_EQUALITY_LIST


def function(NOTE_INDEXES, PATTERN_RED, STARTING_NOTE):
    # define a sharp flat equality dictionary
    
    # return a sequence of notes
    generated_notes = []
    # keep track of the current index at each step
    current_index = 0

    for note in NOTE_INDEXES:
        if NOTE_INDEXES[note] == STARTING_NOTE:
            current_index = note
            generated_notes.append(STARTING_NOTE)
        # find the maximum index to find the period of circulation
        maximum_index = 0
        if note > maximum_index:
            maximum_index = note
    
    for i in PATTERN_RED:
        current_index += i
        if current_index > maximum_index:
            current_index -= (maximum_index + 1)
        generated_notes.append(NOTE_INDEXES[current_index])
    
    #replace same position
    for i in range(len(generated_notes)):
        for j in range(len(generated_notes)-1):
            if generated_notes[i] != generated_notes[j] and generated_notes[i][0] == generated_notes[j][0]:
                for note in SHARP_FLAT_EQUALITY_LIST:
                    if note == generated_notes[j]:
                        duplicate_index = SHARP_FLAT_EQUALITY_LIST[note]
                for note in SHARP_FLAT_EQUALITY_LIST:
                    if duplicate_index == SHARP_FLAT_EQUALITY_LIST[note] and  note != generated_notes[j]:
                        generated_notes[j] = note


    print(generated_notes)

#test case 1 

PATTERN_RED =[2, 1, 2, 2, 1, 2, 2]
STARTING_NOTE = "A"

function(NOTE_INDEXES, PATTERN_RED, STARTING_NOTE)

# test case 2
STARTING_NOTE = "D"

function(NOTE_INDEXES, PATTERN_RED, STARTING_NOTE)