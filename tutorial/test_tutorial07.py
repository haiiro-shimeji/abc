from tutorial07 import main, _createModel, _inModel
import unittest
from parameterized import parameterized
import math
import numpy as np

def _createFixture(t, n):
    return (
        "Case n={}".format(n),
        n,
        np.random.randint(t, size=(n,2)),
    )

class CTest(unittest.TestCase):

    @parameterized.expand([
        (
            "Case1",
            10,
            [
                [9, 4],
                [4, 3],
                [1, 1],
                [4, 2],
                [2, 4],
                [5, 8],
                [4, 0],
                [5, 3],
                [0, 5],
                [5, 2],
            ],
            10,
        ),
        (
            "Case2",
            10,
            list(reversed([
                [9, 4],
                [4, 3],
                [1, 1],
                [4, 2],
                [2, 4],
                [5, 8],
                [4, 0],
                [5, 3],
                [0, 5],
                [5, 2],
            ])),
            10,
        ),
        (
            "Edge1",
            1,
            [
                [1, 1],
            ],
            0,
        ),
        (
            "Edge2",
            2,
            [
                [1, 1],
                [2, 2],
            ],
            0,
        ),
        (
            "Edge3",
            3,
            [
                [1, 1],
                [2, 2],
                [3, 3],
            ],
            0,
        ),
        (
            "Edge4",
            4,
            [
                [0, 0],
                [1, 0],
                [1, 1],
                [0, 1],
            ],
            1,
        ),
        (
            "Edge5",
            4,
            [
                [0, 0],
                [0, 1],
                [1, 1],
                [1, 0],
            ],
            1,
        ),
    ])
    def test_main(self, _, _n, _m, expected):
        self.assertEqual(main(_n, _m), expected)

    @parameterized.expand([
        (
            "Case1",
            [
                [9, 4],
                [4, 3],
                [1, 1],
                [4, 2],
                [2, 4],
                [5, 8],
                [4, 0],
                [5, 3],
                [0, 5],
                [5, 2],
            ],
            (
                [0, 1, 2, 4, 5, 9],
                [
                    [5],
                    [1],
                    [4],
                    [0, 2, 3],
                    [2, 3, 8],
                    [4],
                ],
            )
        ),
    ])
    def test_createModel(self, _, _m, expected):
        self.assertEqual(_createModel(_m), expected)

    @parameterized.expand([
        (
            "Case1",
            _createModel([
                [9, 4],
                [4, 3],
                [1, 1],
                [4, 2],
                [2, 4],
                [5, 8],
                [4, 0],
                [5, 3],
                [0, 5],
                [5, 2],
            ]),
            [5, 3],
            True
        ),
        (
            "Case2",
            _createModel([
                [9, 4],
                [4, 3],
                [1, 1],
                [4, 2],
                [2, 4],
                [5, 8],
                [4, 0],
                [5, 3],
                [0, 5],
                [5, 2],
            ]),
            [1, 0],
            False
        ),
    ])
    def test_inModel(self, _, _m, _p, expected):
        self.assertEqual(_inModel(_m, _p), expected)

    @parameterized.expand([
        _createFixture(5000, 100),
        _createFixture(5000, 500),
        _createFixture(5000, 3000),
    ])
    def test_main_createModel_performance(self, _, __, _m):
        _createModel(_m)
        self.assertTrue(True)

    @parameterized.expand([
        _createFixture(5000, 100),
        _createFixture(5000, 500),
        _createFixture(5000, 3000),
    ])
    def test_main_inModel_performance(self, _, __, _m):
        model = _createModel(_m)
        for i in range(0, 3000):
            self.assertEqual([1, 1] in _m, _inModel(model, [1, 1]))

    """
    @parameterized.expand([
        _createFixture(5000, 100),
        _createFixture(5000, 500),
        #_createFixture(5000, 3000),
    ])
    def test_main_test_performance(self, _, _n, _m):
        main(_n, _m)
        self.assertTrue(True)
    """