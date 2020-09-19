""" B
    https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_b
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

def main(A, B, C, K):
    while A >= B:
        if K == 0:
            return "No"
        B *= 2
        K -= 1
    while B >= C:
        if K == 0:
            return "No"
        C *= 2
        K -= 1

    return "Yes"

if __name__ == "__main__":
    _A, _B, _C = readIntegerSet(3)
    _K = readInteger()

    print(main(_A, _B, _C, _K))