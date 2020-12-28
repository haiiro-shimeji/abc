from E04 import main
import unittest
from parameterized import parameterized

class CTest(unittest.TestCase):

    @parameterized.expand([
        ("2512:C", "DEFGH"),
        ("1:A", "CDEFGH"),
        (":C", "ABDEFGH"),
        ("2345:B", "AGH"),
        ("1256:E", "ABCDH"),
        ("1228:A", "ADEFG"),
        ("5623:B", "AEFGH"),
        ("8157:C", "ABDEFGH"),
        ("74767:E", "ABCFGH"),
        ("88717:D", "ABCEFGH"),
        ("148647:A", "ACDEFH"),
        ("374258:H", "BCDEFH"),
        ("6647768:F", "ABCDEH"),
        ("4786317:E", "ABFGH"),
        ("3456781:C", ""),
        ("225721686547123:C", "CEF"),
        ("2765356148824666:F", "ABCDEH"),
        ("42318287535641783:F", "BDE"),
        ("584423584751745261:D", "FGH"),
        ("8811873415472513884:D", "CFG"),
        ("74817442725737422451:H", "BCDEF"),
        ("223188865746766511566:C", "ABGH"),
        ("2763666483242552567747:F", "ABCG"),
        ("76724442325377753577138:E", "EG"),
        ("327328486656448784712618:B", ""),
        ("4884637666662548114774288:D", "DGH"),
        ("84226765313786654637511248:H", "DEF"),
        ("486142154163288126476238756:A", "CDF"),
        ("1836275732415226326155464567:F", "BCD"),
        ("62544434452376661746517374245:G", "G"),
        ("381352782758218463842725673473:B", "A"),
    ])
    def test(self, _input, expected):
        _paths = [int(s) for s in list(_input.split(':')[0])]
        _rock = _input.split(':')[1].rstrip()
        actual = main(_paths, _rock)
        self.assertEqual(expected, actual)
