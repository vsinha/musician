import unittest
from noteslib import Note
from chords import *


class Tests(unittest.TestCase):
    def test_note_to_id(self):
        self.assertEqual(Note("C4").id, 60)

        # no octave specified, defaults to 4
        self.assertEqual(Note("A#").id, 70)
        self.assertEqual(Note("A#4").id, 70)

        self.assertEqual(Note("D#2").id, 39)

    def test_index_to_note(self):
        self.assertEqual(Note.of_id(60).name, "C4")
        self.assertEqual(Note.of_id(58).name, "A#3")
        self.assertEqual(Note.of_id(39).name, "D#2")

    def test_chords(self):
        self.assertListEqual(
            chord(Note("C"), "major"),
            ["C4", "E4", "G4"],
        )
        self.assertListEqual(chord(Note("C"), "minor"), ["C4", "D#4", "G4"])
        self.assertListEqual(
            chord(Note("A"), "dominant"),
            ["A4", "C#5", "E5", "G5"],
        )
