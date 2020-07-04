from tutorial01 import main
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ("Case1", 5, 9, 2,),
        ("Edge1", 3, 6, 1,),
        ("Edge2", 4, 6, 1,),
        ("Edge3", 100, 300, 0,),
        ("Edge3", 100, 297, 1,),
    ])
    def test_main(self, _, _n, _x, expected):
        self.assertEqual(main(_n, _x), expected)