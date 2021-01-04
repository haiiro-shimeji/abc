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

    # jokerだけの場合はrank=13とする
    if n == 1 and field[0] == 'Jo':
        return (13, n)

    # jocker除外
    field = [f for f in field if f != 'Jo']

    return (RANK.index(field[0][1]), n)

def _availables(hands, field_rank, field_n):
    # 手札をrankでグルーピング.
    hands = dict([
        (k, list(v))
        for k, v in groupby(
            sorted(hands, key=lambda c: RANK.index(c[1])),
            key=lambda c: RANK.index(c[1])
        )
    ])

    logging.debug(hands)

    for rank in hands.keys():
        if rank <= field_rank:
            continue

        cards = hands[rank] \
            + (hands[13] if rank < 13 and field_n > 1 and 13 in hands.keys() else [])

        if len(cards) < field_n:
            continue

        for _ret in _C(len(cards), field_n):
            __ret = list(_ret)
            logging.debug(__ret)
            _cards = [cards[i-1] for i in __ret]
            logging.debug(_cards)
            yield _cards

def _C(n, m):
    k = n
    stack = [k]

    while True:
        if len(stack) < m:
            while k-1 < 1:
                if len(stack) < 1:
                    return
                j = stack.pop()
                k = j

            k -= 1
            stack.append(k)

        if len(stack) == m:
            yield list(stack)
            k = stack.pop()

def _main(_S):
    field = _split_cards(_S.split(',')[0].rstrip())
    hands = _split_cards(_S.split(',')[1].rstrip())

    logging.debug([field, hands])

    # 場のカードのランク、枚数を算出.
    field_rank, field_n = _calc_rank(field)
    logging.debug([field_rank, field_n])

    # 出せる組み合わせを算出.
    availables = list(_availables(hands, field_rank, field_n))

    return ",".join(["".join(sorted(cards)) for cards in availables]) \
        if len(availables) > 0 else '-'

if __name__ == "__main__":
    print(_main(readString()))
