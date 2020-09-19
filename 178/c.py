""" C
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

M = 1000000007

def _pow(n, m):
    ret = 1
    for _ in range(m):
        ret = (ret * n) % M
    return ret

def main(N):
    return (_pow(10, N) - 2 * _pow(9, N) + _pow(8, N)) % M

if __name__ == "__main__":
    _N = readInteger()

    print(main(_N))