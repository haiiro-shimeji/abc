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
        (
            "Case3",
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
            [-1, 0],
            False
        ),
        (
            "Case4",
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
            [1, 1],
            True
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
    def test_main_inModel_performance(self, _, _n, _m):
        model = _createModel(_m)
        self.assertEqual(False, _inModel(model, [-1, -1]))
        self.assertEqual(False, _inModel(model, [5001, 5001]))
        self.assertEqual(False, _inModel(model, [_m[0][0], -1]))
        self.assertEqual(False, _inModel(model, [_m[0][0], 5001]))
        for i in range(0, _n):
            expected = _m[i] in _m
            self.assertEqual(_inModel(model, _m[i]), expected)

    @parameterized.expand([
        _createFixture(5000, 30),
        #_createFixture(5000, 500),
        #_createFixture(5000, 3000),
    ])
    def test_main_test_performance(self, _, _n, _m):
        print(main(_n, _m))
        self.assertTrue(True)
    """
    def test(self):
        self.assertTrue((7180, 3186) in (
            (2928,  106),
            (1988, 4711),
            (2539,  663),
            (2349, 3468),
            (3469, 4663),
            (1031, 2990),
            (  75, 3285),
            ( 263, 2996),
            (3030, 1855),
            (1234, 3772),
            (3514, 3772),
            ( 334, 2046),
            (4807, 2836),
            (  74, 2600),
            ( 611, 4610),
            (2971,  138),
            (3708, 1576),
            (3828, 4634),
            (4311, 4484),
            (4229, 1975),
            (4967, 4621),
            (4105, 3254),
            (4769, 1718),
            ( 918, 2135),
            (2143, 4481),
            (4758, 1521),
            (2564, 1079),
            (1924,  171),
            (3759, 3186),
            (3747,  715)))
    """