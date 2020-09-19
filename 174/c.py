""" C
    https://atcoder.jp/contests/abc173/tasks/abc173_c
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

def main(K):
    if K % 2 == 0:
        return -1

    count = 1
    result = 7 % K
    while True:
        if result == 0:
            break
        result = (result * 10 + 7) % K
        count += 1

    return count

if __name__ == "__main__":
    _K = readInteger()

    print(main(_K))