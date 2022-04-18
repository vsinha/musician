import random

natural_notes: list[str] = ["A", "B", "C", "D", "E", "F", "G"]

all_notes = [
    "A",
    "A#",
    "B",
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#",
]


frequencies = {
    "A": 440.0,
    "A#": 466.16,
    "B": 493.88,
    "C": 523.25,
    "C#": 554.37,
    "D": 587.33,
    "D#": 622.25,
    "E": 659.25,
    "F": 698.46,
    "F#": 739.99,
    "G": 783.99,
    "G#": 830.61,
}


previous_pick = None


def pick_random(notes, never_repeats=False):
    global previous_pick
    note = random.choice(notes)
    if never_repeats:
        while note == previous_pick:
            note = random.choice(notes)
    else:
        if previous_pick == note:
            # Reduce the chance of repeats
            note = random.choice(notes)

    previous_pick = note
    return note
