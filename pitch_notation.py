from math import log2

import noteslib

# Defaults to octave 4 if none is specified, eg "C" is "C4"
# MIDI uses 0-127 so middle_c would be 60
def note_to_index(note: str) -> int:
    base = 0

    last_char = note[-1]
    if last_char.isnumeric():
        # This means the note specifies the octave, eg "C4" or "B#2"
        base = 12 * (int(last_char) + 1)
        note_name = note[:-1]
    else:
        base = 60
        note_name = note

    # print(note, base, note_name, noteslib.all_notes.index(note_name))

    # middle C is 0, which means A is -3
    return base + noteslib.all_notes.index(note_name)


def index_to_note(idx: int) -> str:
    note = noteslib.all_notes[(idx - 60) % 12]
    octave = 4 + ((idx - 60) // 12)
    return note + str(octave)


# https://en.wikipedia.org/wiki/Pitch_class#Integer_notation
def pitch(note_integer):
    return 69 + 12 * log2(note_integer / 440)


chords = {"dominant": [0, 4, 7, 10]}


def get_chord(root: int):
    pass
