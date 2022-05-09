import unittest
from notes import Note
from scales import scale


class Tests(unittest.TestCase):
    def test_creating_some_scales(self):
        self.assertListEqual(
            scale(Note("C"), "major"), ["C", "D", "E", "F", "G", "A", "B", "C5"]
        )
        self.assertListEqual(
            scale(Note("A"), "minor"), ["A", "B4", "C5", "D5", "E5", "F5", "G5", "A5"]
        )
        self.assertListEqual(
            scale(Note("A"), "major"),
            ["A", "B4", "C#5", "D5", "E5", "F#5", "G#5", "A5"],
        )
