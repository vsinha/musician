from typing import Tuple

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


class Note:
    name: str
    index: int
    octave: int

    # Defaults to octave 4 if none is specified, eg "C" is "C4"
    # MIDI uses 0-127 so middle_c would be 60
    @staticmethod
    def parse_note_name_to_name_id_octave(note: str) -> Tuple[str, int, int]:
        note = note.upper()

        last_char = note[-1]
        if last_char.isnumeric():
            # This means the note specifies the octave, eg "C4" or "B#2"
            octave = int(last_char)
            note_name = note[:-1]
        else:
            octave = 4
            note_name = note

        return (note_name, all_note_names.index(note_name), octave)

    @staticmethod
    def id_to_name(index: int) -> str:
        return all_note_names[index]

    def __init__(self, name, octave=4):
        self.octave = octave
        if isinstance(name, str):
            self.name, self.index, octave = Note.parse_note_name_to_name_id_octave(name)

            if any(chr.isdigit() for chr in name):
                self.octave = octave

        elif isinstance(name, int):
            self.name = Note.id_to_name(name)
            self.index = name

    @classmethod
    def of_id(cls, id: int):
        return cls(Note.id_to_name(id))

    def __eq__(self, other):
        if isinstance(other, Note):
            return self.index == other.index and self.octave == other.octave
        elif isinstance(other, str):
            return self == Note(other)
        elif isinstance(other, int):
            return self == Note.of_id(other)
        else:
            return False

    # https://davywybiral.blogspot.com/2010/09/procedural-music-with-pyaudio-and-numpy.html
    def frequency(self):
        base_frequency = 16.35159783128741 * 2.0 ** (float(self.index) / 12.0)
        return base_frequency * (2.0 ** self.octave)

    def transpose(self, halfsteps):
        octave_delta, note = divmod(self.index + halfsteps, 12)
        return Note(note, self.octave + octave_delta)

    def __str__(self) -> str:
        return self.name + str(self.octave)

    def __repr__(self) -> str:
        return self.__str__()
