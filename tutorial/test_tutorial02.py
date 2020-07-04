from tutorial02 import main, f
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ("105", 105, 8,),
        ("135", 135, 8,),
        ("165", 165, 8,),
        ("189", 189, 8,),
        ("195", 195, 8,),
    ])
    def test_f(self, _, _n, expected):
        self.assertEqual(f(_n), expected)

    @parameterized.expand([
        ("Case1", 105, 1,),
        ("Case2", 200, 5,),
    ])
    def test_main(self, _, _n, expected):
        self.assertEqual(main(_n), expected)
