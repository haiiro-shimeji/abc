""" A
    https://atcoder.jp/contests/abc175/tasks/abc175_a
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

def main(S):
    candidate = 0
    best = 0

    for c in list(S.rstrip()):
        if c == "S":
            if candidate > best:
                best = candidate
            candidate = 0
        else:
            candidate += 1

    if candidate > best:
        best = candidate

    return best

if __name__ == "__main__":
    _S = readString()

    print(main(_S))