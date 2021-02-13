from main import _main
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ( "1728398", "bc" ),
        ( "789", "-" ),
        ( "274", "ac" ),
        ( "185", "abc" ),
        ( "396", "ab" ),
        ( "1278", "abc" ),
        ( "7659832", "a" ),
        ( "178", "bc" ),
        ( "189", "ab" ),
        ( "197", "a" ),
        ( "278", "ac" ),
        ( "289", "bc" ),
        ( "297", "a" ),
        ( "378", "ac" ),
        ( "389", "b" ),
        ( "397", "ab" ),
        ( "478", "c" ),
        ( "489", "bc" ),
        ( "497", "ab" ),
        ( "578", "bc" ),
        ( "589", "b" ),
        ( "597", "ac" ),
        ( "678", "c" ),
        ( "689", "ab" ),
        ( "697", "ac" ),
        ( "899", "b" ),
        ( "7172", "ac" ),
        ( "54787", "bc" ),
        ( "83713", "bc" ),
        ( "149978", "-" ),
        ( "159735", "abc" ),
        ( "1449467", "abc" ),
        ( "9862916", "b" ),
        ( "96112873", "ab" ),
        ( "311536789", "-" ),
        ( "281787212994", "abc" ),
        ( "697535114542", "ac" ),
    ])
    def test(self, _input, expected):
        self.assertEqual(_main(_input), expected)
