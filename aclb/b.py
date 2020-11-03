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

def main(A, B, C, D):
    if (A <= C and C <= B) \
        or (A <= D and D <= B) \
        or (C <= A and A <= D) \
        or (C <= B and B <= D):
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    _A, _B, _C, _D = readIntegerSet(4)

    print(main(_A, _B, _C, _D))
