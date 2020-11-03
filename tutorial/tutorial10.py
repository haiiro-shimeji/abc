""" tutorial10
    http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja
"""
import sys
import math
import copy
from functools import reduce
from itertools import combinations
from bisect import bisect_left

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

def main(N, A, Q, M):
    """ main
    """
    A = sorted(A)

    def _try(m):
        for n in range(N):
            for c in combinations(A, n):
                if m == sum(c):
                    return "yes"
        return "no"

    for m in M:
        print(_try(m))

if __name__ == "__main__":
    _N = readInteger()
    _A = readIntegerSet(_N)
    _Q = readInteger()
    _M = readIntegerSet(_Q)

    main(_N, _A, _Q, _M)
