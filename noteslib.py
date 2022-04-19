from dataclasses import dataclass
from math import log2

natural_note_names: list[str] = [
    "C",
    "D",
    "E",
    "F",
    "G",
    "A",
    "B",
]

all_note_names = [
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#",
    "A",
    "A#",
    "B",
]


frequencies = {
    "C": 523.25,
    "C#": 554.37,
    "D": 587.33,
    "D#": 622.25,
    "E": 659.25,
    "F": 698.46,
    "F#": 739.99,
    "G": 783.99,
    "G#": 830.61,
    "A": 440.0,
    "A#": 466.16,
    "B": 493.88,
}


@dataclass
class Note:
    name: str

    # The MIDI note number of the note in question
    id: int

    # Defaults to octave 4 if none is specified, eg "C" is "C4"
    # MIDI uses 0-127 so middle_c would be 60
    @staticmethod
    def name_to_id(note: str) -> int:
        base = 0

        last_char = note[-1]
        if last_char.isnumeric():
            # This means the note specifies the octave, eg "C4" or "B#2"
            base = 12 * (int(last_char) + 1)
            note_name = note[:-1]
        else:
            base = 60
            note_name = note

        # middle C is 0, which means A is -3
        return base + all_note_names.index(note_name)

    @staticmethod
    def id_to_name(idx: int) -> str:
        note = all_note_names[(idx - 60) % 12]
        octave = 4 + ((idx - 60) // 12)

        return note + str(octave)

    def __init__(self, name, id=None):
        self.name = name
        if id is None:
            self.id = Note.name_to_id(name)
        else:
            self.id = id

    @classmethod
    def of_id(cls, id: int):
        return cls(Note.id_to_name(id))

    def __eq__(self, other):
        if isinstance(other, Note):
            return self.id == other.id
        elif isinstance(other, str):
            return self == Note(other)
        elif isinstance(other, int):
            return self == Note.of_id(other)
        else:
            return False

    # https://en.wikipedia.org/wiki/Pitch_class#Integer_notation
    def to_pitch(self):
        return 9 + 12 * log2(self.id / 440)
