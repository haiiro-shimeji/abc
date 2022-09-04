""" test_b.py
"""

from unittest import TestCase
from .c import main
from parameterized import parameterized

class Test(TestCase):
    """ Test
    """

    @parameterized.expand([
        (
            4, 2, [5, 4, -1, 8],
            15
        ),
        (
            10, 4, [-3, 1, -4, 1, -5, 9, -2, 6, -5, 3],
            31
        ),
        (
            10, 10, [1] * 10,
            55
        ),
        (
            200000, 200000, [1] * 200000,
            20000100000
        ),
        (
            200000, 100000, [1] * 200000,
            5000050000
        ),
    ])
    def test_main(self, N, M, A, expected):
        """ test_main
        """
        self.assertEqual(main(N, M, A), expected)
