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

GRAPH = {
    'A': ['D', 'C', 'B'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'F', 'B'],
    'D': ['E', 'F', 'A'],
    'E': ['F', 'D', 'B'],
    'F': ['D', 'E', 'C'],
}

def _main(_S):
    cmds = list(_S.rstrip())

    prev = 'B'
    cur = 'A'

    result = [cur]

    for c in cmds:
        routes = GRAPH[cur]
        to = routes.index(prev)

        if 'r' == c:
            to = (to - 1) % 3
        elif 'l' == c:
            to = (to + 1) % 3

        prev = cur
        cur = routes[to]

        result.append(cur)

    return ''.join(result)

if __name__ == "__main__":
    print(_main(readString()))
