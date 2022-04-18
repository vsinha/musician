import noteslib

scales = {
    "major": "WWHWWWH",
    "pentatonic": "3WW3W",
    "minor": "WHWWHWW",
    "harmonic_minor": "WHWWH3H",
    "dorian": "WHWWWHW",
    "mixolydian": "WWHWWHW",
}


def get_scale(key, which_scale):
    steps = scales[which_scale]
    increments = []

    for char in steps:
        if char == "W":
            increments.append(2)
        elif char == "3":
            increments.append(3)
        elif char == "H":
            increments.append(1)
        else:
            print("Something's wrong, got a ", char)

    # find our starting index
    idx = noteslib.all_notes.index(key)

    notes = [key]
    for increment in increments:
        idx = (idx + increment) % len(noteslib.all_notes)
        note = noteslib.all_notes[idx]
        notes.append(note)

    # we want our scale to not re-include the note we started with
    notes = notes[:-1]

    print("key:", key, which_scale, ", notes:", notes)
    return notes
