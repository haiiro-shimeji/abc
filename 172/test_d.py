from d import main, f, _f
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ("1 expects 1", 1, 1,),
        ("2 expects 2", 2, 2,),
        ("4 expects 3", 4, 3,),
        ("6 expects 4", 6, 4,),
        ("10000000 expects ?", 10000000, 64,),
    ])
    def test_f(self, _, _x, expected):
        self.assertEqual(f(_x), expected)

    @parameterized.expand([
        ("", 9999999, [],),
    ])
    def test_f(self, _, _x, expected):
        self.assertEqual(_f(_x), expected)

    """
    @parameterized.expand([
        ("Case1", 4, 23,),
        ("Case2", 100, 26879,),
        ("Case3", 10000000, 838627288460105,),
    ])
    def test_f(self, _, _n, expected):
        self.assertEqual(main(_n), expected)
    """