import unittest
from scales import get_scale


class Tests(unittest.TestCase):
    def test_creating_some_scales(self):
        self.assertListEqual(
            get_scale("C", "major"), ["C", "D", "E", "F", "G", "A", "B"]
        )
        self.assertListEqual(
            get_scale("A", "minor"), ["A", "B", "C", "D", "E", "F", "G"]
        )
        self.assertListEqual(
            get_scale("A", "major"), ["A", "B", "C#", "D", "E", "F#", "G#"]
        )
