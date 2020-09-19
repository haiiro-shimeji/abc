from .bisect_search import create_model, search
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ("Case1", [1,4,2,9,6], 1, 0,),
        ("Case2", [1,4,2,9,6], 0, -1,),
        ("Case3", [1,4,2,9,6], 10, -1,),
        ("Case4", [1,4,2,9,6], 9, 3,),
        ("Case5", [1,4,2,9,6], 4, 1,),
    ])
    def test_search(self, _, a, e, expected):
        m = create_model(a)
        self.assertEqual(search(e, m), expected)