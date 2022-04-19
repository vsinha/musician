from notes import Note

chords = {
    "major": [0, 4, 7],
    "major seventh": [0, 4, 7, 11],
    "minor": [0, 3, 7],
    "minor seventh": [0, 3, 7, 10],
    "dominant": [0, 4, 7, 10],
}


def chord(root: Note, chord):
    return [Note.of_id(root.id + note) for note in chords[chord]]
