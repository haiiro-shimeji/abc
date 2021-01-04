from ord5dahimi import _main as _main
from ord5dahimi import _C as _C
from ord5dahimi import _split_cards as _split_cards
import unittest
from parameterized import parameterized

def _sort(ret):
    return ','.join(sorted([''.join(sorted(_split_cards(s))) for s in ret.split(',')]))

class CTest(unittest.TestCase):

    @parameterized.expand([
        ( "DJ,", "-" ),
        ( "H7,HK", "HK" ),
        ( "S3,D4D2", "D4,D2" ),
        ( "S9,C8H4", "-" ),
        ( "S6,S7STCK", "CK,ST,S7" ),
        ( "H4,SAS8CKH6S4", "S8,CK,H6,SA" ),
        ( "ST,D6S8JoC7HQHAC2CK", "Jo,C2,CK,HA,HQ" ),
        ( "SA,HAD6S8S6D3C4H2C5D4CKHQS7D5", "H2" ),
        ( "S2,D8C9D6HQS7H4C6DTS5S6C7HAD4SQ", "-" ),
        ( "Jo,HAC8DJSJDTH2", "-" ),
        ( "S4Jo,CQS6C9DQH9S2D6S3", "DQCQ,D6S6,H9C9" ),
        ( "CTDT,S9C2D9D3JoC6DASJS4", "JoC2,SJJo,DAJo" ),
        ( "H3D3,DQS2D6H9HAHTD7S6S7Jo", "JoHA,JoD6,JoH9,D6S6,D7S7,JoS6,HTJo,JoDQ,S2Jo,JoD7,JoS7" ),
        ( "D5Jo,CQDAH8C6C9DQH7S2SJCKH5", "CQDQ" ),
        ( "C7H7,S7CTH8D5HACQS8JoD6SJS5H4", "HAJo,JoSJ,H8S8,H8Jo,CQJo,CTJo,JoS8" ),
        ( "SAHA,S7SKCTS3H9DJHJH7S5H2DKDQS4", "-" ),
        ( "JoC8,H6D7C5S9CQH9STDTCAD9S5DAS2CT", "CTDT,H9D9,S9D9,DACA,CTST,H9S9,DTST" ),
        ( "HTST,SJHJDJCJJoS3D2", "DJCJ,SJDJ,JoHJ,CJHJ,SJJo,HJSJ,DJJo,JoCJ,JoD2,SJCJ,DJHJ" ),
        ( "C7D7,S8D8JoCTDTD4CJ", "D8S8,JoS8,CTJo,DTJo,JoCJ,CTDT,D8Jo" ),
        ( "DJSJ,DTDKDQHQJoC2", "JoDK,HQDQ,DQJo,C2Jo,JoHQ" ),
        ( "C3H3D3,CKH2DTD5H6S4CJS5C6H5S9CA", "S5H5D5" ),
        ( "D8H8S8,CQHJCJJoHQ", "JoCQHQ,JoHJCJ" ),
        ( "H6D6S6,H8S8D8C8JoD2H2", "D2H2Jo,D8JoS8,D8S8C8,C8D8H8,JoC8S8,H8JoC8,S8H8C8,JoS8H8,C8JoD8,D8H8S8,D8JoH8" ),
        ( "JoD4H4,D3H3S3C3CADASAD2", "DACASA" ),
        ( "DJHJSJ,SQDQJoHQCQC2CA", "SQJoCQ,DQCQJo,JoSQHQ,SQCQHQ,DQHQSQ,HQDQCQ,HQDQJo,SQDQCQ,CQJoHQ,SQJoDQ" ),
        ( "H3D3Jo,D4SKH6CTS8SAS2CQH4HAC5DADKD9", "HASADA" ),
        ( "C3JoH3D3,S2S3H7HQCACTC2CKC6S7H5C7", "-" ),
        ( "H5C5S5D5,C7S6D6C3H7HAH6H4C6HQC9", "C6D6S6H6" ),
        ( "H7S7C7D7,S5SAH5HAD5DAC5CA", "SADACAHA" ),
        ( "D4H4S4C4,S6SAH6HAD6DAC6CAJo", "C6H6S6D6,SAJoDACA,S6H6C6Jo,SACAJoHA,HADASAJo,HADAJoCA,CADAHASA,D6C6JoH6,S6D6C6Jo,H6JoS6D6" ),
        ( "DTCTSTHT,S3SQH3HQD3DQC3CQJo", "HQSQJoDQ,SQCQDQJo,DQCQHQJo,SQHQJoCQ,CQDQHQSQ" ),
        ( "JoS8D8H8,S9DTH9CTD9STC9CAC2", "H9C9D9S9" ),
    ])
    def test(self, _input, _expected):
        self.assertEqual(_sort(_main(_input)), _sort(_expected))

    @parameterized.expand([
        (1, 1, [[1]]),
        (3, 3, [[3, 2, 1]]),
        (3, 1, [[3], [2], [1]]),
        (4, 2, [[4, 3], [4, 2], [4, 1], [3, 2], [3, 1], [2, 1]]),
        (5, 2, [[5, 4], [5, 3], [5, 2], [5, 1], [4, 3], [4, 2], [4, 1], [3, 2], [3, 1], [2, 1]]),
    ])
    def test_C(self, n, m, expected):
        self.assertEqual(list(_C(n, m)), expected)