""" C
    https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_c
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

def main(N, K, A):
    for i in range(0, N-K):
        print("Yes" if A[i] < A[i+K] else "No")

if __name__ == "__main__":
    _N, _K = readIntegerSet(2)
    _A = readIntegerSet(_N)

    main(_N, _K, _A)