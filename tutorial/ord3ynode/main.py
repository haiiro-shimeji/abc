""" http://nabetani.sakura.ne.jp/hena/ord3ynode/
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

NODES = ['A', 'B', 'C', 'D', 'E', 'F']

GRAPH = {
    0: [3, 2, 1],
    1: [0, 2, 4],
    2: [0, 5, 1],
    3: [4, 5, 0],
    4: [5, 3, 1],
    5: [3, 4, 2],
}

def _main(_S):
    cmds = list(_S.rstrip())

    prev = 1
    cur = 0

    result = ['A']

    for c in cmds:
        routes = GRAPH[cur]
        to = routes.index(prev)

        if 'r' == c:
            to = (to - 1) % 3
        elif 'l' == c:
            to = (to + 1) % 3

        prev = cur
        cur = routes[to]

        result.append(NODES[cur])

    return ''.join(result)

if __name__ == "__main__":
    print(_main(readString()))
