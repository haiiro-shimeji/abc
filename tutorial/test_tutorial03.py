from tutorial03 import main
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ("Case1", "ATCODER", 3,),
        ("Case2", "HATAGAYA", 5,),
        ("Case3", "SHINJUKU", 0,),
        ("Edge1", "ATCGATCG", 8,),
    ])
    def test_main(self, _, _s, expected):
        self.assertEqual(main(_s), expected)
