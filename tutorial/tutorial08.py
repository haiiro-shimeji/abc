""" tutorial08
    https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b
"""
import sys
import math
from functools import reduce
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

def main(N, M):
    """ main
    """
    A, B = list(zip(*M))

    s = sorted(A)[N//2]
    g = sorted(B)[N//2]

    return sum([abs(s-a) + abs(a-b) + abs(g-b) for a, b in M])

if __name__ == "__main__":
    _N = readInteger()
    _M = readIntegerMatrix(_N, 2)

    print(main(_N, _M))
