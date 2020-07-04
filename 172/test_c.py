from c import main
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        (
            "Case1",
            3, 4, 240,
            [60, 90, 120],
            [80, 150, 80, 150],
            3
        ),
        (
            "Case2",
            3, 4, 730,
            [60, 90, 120],
            [80, 150, 80, 150],
            7
        ),
        (
            "Case3",
            5, 4, 1,
            [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],
            [1000000000, 1000000000, 1000000000, 1000000000],
            0
        ),
        (
            "A is just",
            1, 0, 1,
            [1],
            [],
            1
        ),
        (
            "A is not enough",
            2, 0, 3,
            [1, 1],
            [],
            2
        ),
        (
            "A is over",
            2, 0, 3,
            [1,5],
            [],
            1
        ),
        (
            "B is just",
            0, 1, 1,
            [],
            [1],
            1
        ),
        (
            "B is not enough",
            0, 2, 3,
            [],
            [1, 1],
            2
        ),
        (
            "B is over",
            0, 2, 3,
            [],
            [1, 5],
            1
        ),
    ])
    def test_main(self, _, _n, _m, _k, _a, _b, expected):
        self.assertEquals(main(_n, _m, _k, _a, _b), expected)
        