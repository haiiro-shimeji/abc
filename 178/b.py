""" B
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
    return [readIntegerSet(m) for _ in range(0, n)]

def main(_a, _b, _c, _d):
    return max([_a * _c, _a * _d, _b * _c, _b * _d])


if __name__ == "__main__":
    _a, _b, _c, _d = readIntegerSet(4)

    print(main(_a, _b, _c, _d))
