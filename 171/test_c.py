from c import main
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ("Case1", 2, "b",),
        ("Case2", 27, "aa",),
        ("Case3", 123456789, "jjddja",),
        ("Edge1", 1, "a",),
        ("Edge2", 26, "z",),
        ("Edge3", 1000000000000001, "gbdpxgrzxjm",),
    ])
    def test_main(self, _, _n, expected):
        self.assertEqual(main(_n), expected)