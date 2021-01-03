""" http://nabetani.sakura.ne.jp/hena/ord5dahimi/
"""
import os
import sys
import math
from functools import reduce
from itertools import groupby
import logging

logging.getLogger().setLevel(int(os.getenv('LOG_LEVEL', 40)))

def readString():
    return sys.stdin.readline()

def readInteger():
    return int(readString())

def readStringSet(n):
    return sys.stdin.readline().split(" ")[:n]

def readIntegerSet(n):
    return list(map(int, readStringSet(n)))

def readIntegerMatrix(n, m):
    return reduce(lambda acc, _: acc + [readIntegerSet(m)], range(0, n), [])

def _split_cards(_s):
    return [_s[i : i + 2] for i in range(0, len(_s), 2)]

RANK = ['3','4','5','6','7','8','9','T','J','Q','K','A','2','o']

def _calc_rank(field):
    n = len(field)

    # jokerだけの場合はrank=15とする
    if n == 1 and field[0] == 'Jo':
        return (15, n)

    # jocker除外
    field = [f for f in field if f != 'Jo']

    return (RANK.index(field[0][1]), n)


def _main(_S):
    field = _split_cards(_S.split(',')[0].rstrip())
    hands = _split_cards(_S.split(',')[1].rstrip())

    logging.debug([field, hands])

    # 場のカードのランク、枚数を算出.
    field_rank, field_n = _calc_rank(field)
    logging.debug([field_rank, field_n])

    # 手札をrankでグルーピング.
    hands = {k: v for h in hands}

    # 場のカードより弱いものを除外.

    # ランクごとに出せる組み合わせを算出.

if __name__ == "__main__":
    print(_main(readString()))
