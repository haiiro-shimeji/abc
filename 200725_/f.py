""" F
    https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_f
"""
import sys
import math
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

def main(N, M):
    S = sum([min(x, y) * p for x, y, p in M])
    print(S)

    M = sorted(zip(range(0, N), M), key=lambda t: t[1][2])
    print(M)

if __name__ == "__main__":
    _N = readInteger()
    _M = readIntegerMatrix(_N, 3)

    print(main(_N, _M))