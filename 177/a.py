""" A
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
    return [lambda _: readIntegerSet(m) for _ in range(0, n)]

def main(D, T, S):
    return "Yes" if T * S >= D else "No"

if __name__ == "__main__":
    _D, _T, _S = readIntegerSet(3)

    print(main(_D, _T, _S))