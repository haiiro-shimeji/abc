""" A
    https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_a
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

def main(X):
    if X <= 599:
        return 8
    if X <= 799:
        return 7
    if X <= 999:
        return 6
    if X <= 1199:
        return 5
    if X <= 1399:
        return 4
    if X <= 1599:
        return 3
    if X <= 1799:
        return 2
    if X <= 1999:
        return 1

if __name__ == "__main__":
    _X = readInteger()

    print(main(_X))