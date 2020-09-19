""" tutorial09
    https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d
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

def main(N, X, M, A):
    """ main
    """
    for i in range(1, M):
        x = X[0][0] - A[i][0]
        y = X[0][1] - A[i][1]

        for j in range(1, N):
            X[j][0] + x, X[j][1] + y

if __name__ == "__main__":
    _N = readInteger()
    _X = readIntegerMatrix(_N, 2)
    _M = readInteger()
    _A = readIntegerMatrix(_M, 2)

    print(main(_N, _X, _M, _A))
