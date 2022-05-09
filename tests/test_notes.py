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
        self.assertEqual(Note("D#", octave=5).octave, 5)

    def test_index_to_note(self):
        self.assertEqual(Note(0), "C4")
        self.assertEqual(Note(10, octave=3), "A#3")
        self.assertEqual(Note(3, octave=2), "D#2")

    def test_frequency(self):
        self.assertAlmostEqual(Note("A3").frequency(), 220.00, places=2)
        self.assertAlmostEqual(Note("B3").frequency(), 246.94, places=2)
        self.assertAlmostEqual(Note("C").frequency(), 261.63, places=2)
        self.assertAlmostEqual(Note("D").frequency(), 293.66, places=2)
        self.assertAlmostEqual(Note("A").frequency(), 440.0, places=2)
        self.assertAlmostEqual(Note("C5").frequency(), 523.25, places=2)
