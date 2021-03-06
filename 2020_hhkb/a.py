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

def main(S, T):
    if "Y" == S:
        return T.upper()

    return T

if __name__ == "__main__":
    _S = readString().rstrip()
    _T = readString().rstrip()

    print(main(_S, _T))