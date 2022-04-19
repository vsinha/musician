import unittest

from notes import Note


class Test(unittest.TestCase):
    def test_note_to_id(self):
        self.assertEqual(Note("C").name, "C")
        self.assertEqual(Note("C").index, 0)
        self.assertEqual(Note("C").octave, 4)

        # no octave specified, defaults to 4
        self.assertEqual(Note("A#").index, 10)
        self.assertEqual(Note("A#").octave, 4)

        self.assertEqual(Note("D#2").index, 3)
        self.assertEqual(Note("D#2").octave, 2)

        self.assertEqual(Note("D#5").octave, 5)

    def test_index_to_note(self):
        self.assertEqual(Note(0), "C4")
        self.assertEqual(Note(10, octave=3), "A#3")
        self.assertEqual(Note(3, octave=2), "D#2")

    def test_frequency(self):
        self.assertEqual(Note("A").frequency(), 440.0)
        self.assertAlmostEqual(Note("B").frequency(), 493.88, places=2)
