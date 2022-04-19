import unittest
from notes import Note
from chords import *


class Tests(unittest.TestCase):
    def test_chords(self):
        # self.assertListEqual(
        #     chord(Note("C"), "major"),
        #     ["C4", "E4", "G4"],
        # )
        # self.assertListEqual(chord(Note("C"), "minor"), ["C4", "D#4", "G4"])
        self.assertListEqual(
            chord(Note("A"), "dominant"),
            ["A4", "C#5", "E5", "G5"],
        )


if __name__ == "__main__":
    unittest.main()
