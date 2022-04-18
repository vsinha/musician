import unittest
from pitch_notation import note_to_index, index_to_note


class Tests(unittest.TestCase):
    def test_note_to_index(self):
        self.assertEqual(note_to_index("C4"), 60)

        # no octave specified, defaults to 4
        self.assertEqual(note_to_index("A#"), 70)
        self.assertEqual(note_to_index("A#4"), 70)

        self.assertEqual(note_to_index("D#2"), 39)

    def test_index_to_note(self):
        self.assertEqual(index_to_note(60), "C4")
        self.assertEqual(index_to_note(58), "A#3")
        self.assertEqual(index_to_note(39), "D#2")


if __name__ == "__main__":
    # begin the unittest.main()
    unittest.main()
