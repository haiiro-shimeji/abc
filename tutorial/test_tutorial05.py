from tutorial05 import main
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ("Case1", 1500, 2000, 1600, 3, 2, 7900,),
        ("Case2", 1500, 2000, 1900, 3, 2, 8500,),
        ("Case3", 1500, 2000, 500, 90000, 100000, 100000000,),
        ("Edge1", 1500, 800, 500, 3, 2, 3000,),
        ("Edge2", 1100, 800, 500, 3, 2, 3000,),
        ("Edge3", 1500, 800, 500, 2, 3, 2800,),
        ("Edge4", 1100, 800, 500, 2, 3, 2800,),
    ])
    def test_main(self, _, _a, _b, _c, _x, _y, expected):
        self.assertEqual(main(_a, _b, _c, _x, _y), expected)
