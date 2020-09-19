""" B
    https://atcoder.jp/contests/abc173/tasks/abc173_b
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

def main(N, D, XY):
    count = 0

    D2 = math.pow(D, 2)

    for xy in XY:
        if math.pow(xy[0], 2) + math.pow(xy[1], 2) <= D2:
            count += 1

    return count

if __name__ == "__main__":
    _N, _D = readIntegerSet(2)
    _XY = readIntegerMatrix(_N, 2)

    print(main(_N, _D, _XY))
