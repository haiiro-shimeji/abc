from main import _main
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ("b", "AB" ),
        ("l", "AD" ),
        ("r", "AC" ),
        ("bbb", "ABAB" ),
        ("rrr", "ACBA" ),
        ("blll", "ABCAB" ),
        ("llll", "ADEBA" ),
        ("rbrl", "ACADE" ),
        ("brrrr", "ABEDAB" ),
        ("llrrr", "ADEFDE" ),
        ("lrlll", "ADFEDF" ),
        ("lrrrr", "ADFCAD" ),
        ("rllll", "ACFDAC" ),
        ("blrrrr", "ABCFEBC" ),
        ("brllll", "ABEFCBE" ),
        ("bbrllrrr", "ABACFDEFD" ),
        ("rrrrblll", "ACBACABCA" ),
        ("llrlrrbrb", "ADEFCADABA" ),
        ("rrrbrllrr", "ACBABEFCAD" ),
        ("llrllblrll", "ADEFCBCADEB" ),
        ("lrrlllrbrl", "ADFCBEFDFCB" ),
        ("lllrbrrlbrl", "ADEBCBACFCAB" ),
        ("rrrrrrlrbrl", "ACBACBADFDEB" ),
        ("lbrbbrbrbbrr", "ADABABEBCBCFE" ),
        ("rrrrlbrblllr", "ACBACFCACFDAB" ),
        ("lbbrblrlrlbll", "ADADFDABCFDFED" ),
        ("rrbbrlrlrblrl", "ACBCBADFEBEFDA" ),
        ("blrllblbrrrrll", "ABCFDADEDABEDFE" ),
        ("blrllrlbllrrbr", "ABCFDABCBEFDEDA" ),
        ("lbrbbrllllrblrr", "ADABABEFCBEDEBCF" ),
        ("rrrrbllrlrbrbrr", "ACBACABCFDEDADFC" ),
    ])
    def test(self, _input, expected):
        self.assertEqual(_main(_input), expected)
