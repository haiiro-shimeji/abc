""" A
    https://atcoder.jp/contests/abc173/tasks/abc173_a
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

def main(X):
    return "Yes" if X >= 30 else "No"

if __name__ == "__main__":
    _X = readInteger()

    print(main(_X))