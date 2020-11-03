from c import _pattern
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ("Case1", 1, [[0], [1]]),
        ("Case2", 2, [[0, 0], [0, 1], [1, 0], [1, 1]]),
    ])
    def test_pattern(self, _, _n, expected):
        self.assertEqual(_pattern(_n), expected)