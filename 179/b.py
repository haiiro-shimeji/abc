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

def main(N, D):
    count = 0
    for d in D:
        if d[0] == d[1]:
            count += 1
            if count == 3:
                return "Yes"
        else:
            count = 0

    return "No"


if __name__ == "__main__":
    _N = readInteger()
    _D = readIntegerMatrix(_N, 2)

    print(main(_N, _D))
