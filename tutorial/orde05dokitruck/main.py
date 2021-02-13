""" http://nabetani.sakura.ne.jp/hena/orde05dokitruck/
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

BLOCK = [
    [[1,2],[2,3],[3]],
    [[1,3],[2],[2,3]],
    [[1,3],[1,2],[3]],
    [[1],[1,2],[2,3]],
    [[1],[2,3],[1,3]],
    [[1,2],[2],[1,3]],
    [[1],[],[3]],
    [[],[2],[3]],
    [[1],[2],[]],
]

def _effect(routes, block):
    return [
        set(sum([block[n-1] for n in r], []))
        for r in routes
    ]

def _main(_S):
    blocks = [BLOCK[int(c)-1] for c in list(_S)]

    routes = reduce(_effect, blocks, [{1},{2},{3}])

    logging.debug([len(r) for r in routes])

    result = [list("abc")[i] for i, r in enumerate(routes) if r]
    return "".join(result) if result else "-"

if __name__ == "__main__":
    print(_main(readString()))
