import notes

scales = {
    "major": "WWHWWWH",
    "pentatonic": "3WW3W",
    "minor": "WHWWHWW",
    "harmonic_minor": "WHWWH3H",
    "dorian": "WHWWWHW",
    "mixolydian": "WWHWWHW",
}


def scale(root: notes.Note, which_scale):
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
            raise Exception(
                "Unexpected character when trying to construct a scale:",
                char,
                "root: ",
                root,
                "steps: ",
                steps,
            )

    # starting at the root
    id = root.id

    scale = [root]
    for increment in increments:
        id = id + increment
        scale.append(notes.Note.of_id(id))

    # we want our scale to not re-include the note we started with
    # TODO maybe we do want the root one octave up... idk yet
    scale = scale[:-1]

    return scale
