""" test_b.py
"""

from unittest import TestCase
from b import main
from parameterized import parameterized

class TestB(TestCase):
    """ TestB
    """

    @parameterized.expand([
        (
            "test1",
            5, [1], [1, 1, 1, 1, 1],
            "5"
        ),
        (
            "test2",
            2, [1, 2], [1, 2],
            "1 2"
        ),
        (
            "test N is 1",
            1, [1], [1],
            "1"
        ),
        (
            "test stop_to_right is true.",
            5, [1], [1, 1, 1, 1, 1],
            "5"
        ),
        (
            "test stop_to_other is true.",
            5, [1, 2], [1, 2, 1, 2, 1],
            "3 4"
        ),
        (
            "test stop_to_right and stop_to_other is true.",
            5, [1, 2], [1, 2, 1, 2, 1, 2, 2],
            "3 5"
        )
    ])
    def test_main(self, _, N, A, L, expected):
        """ test_main
        """
        self.assertEqual(main(N, A, L), expected)
