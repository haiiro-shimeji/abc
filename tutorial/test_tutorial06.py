from tutorial06 import main
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ("Case1", 4, "0224", 3,),
        ("Case2", 6, "123123", 17,),
        ("Case3", 19, "3141592653589793238", 329,),
    ])
    def test_main(self, _, _n, _s, expected):
        self.assertEqual(main(_n, _s), expected)
