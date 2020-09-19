""" C
    https://atcoder.jp/contests/abc175/tasks/abc175_c
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

def _pattern(N):
    if N > 1:
        pa = _pattern(N-1)
        return [[0] + p for p in pa] + [[1] + p for p in pa]
    else:
        return [[0], [1]]

def main(X, K, D):
    if abs(X) > abs(D) * K:
        return abs(X) - abs(D) * K
    else:
        k = abs(X) // abs(D)
        if (K - k) % 2 == 0:
            return abs(X) - k * abs(D)
        else:
            return min(abs(abs(X) - (k+1) * abs(D)), abs(abs(X) - (k-1) * abs(D)))

if __name__ == "__main__":
    _X, _K, _D = readIntegerSet(3)

    print(main(_X, _K, _D))