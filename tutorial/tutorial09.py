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

def main(M, X, N, A):
    """ main
    """
    Ax = {x:x for x, _ in A}
    Ay = {y:y for _, y in A}

    # X[0] が A[n] に一致すると仮定し、X[1:m] に相当する点が存在するかどうかを確認する.
    # n x m x log(n) = 200000 x 3

    for n in range(0, N):
        x = A[n][0] - X[0][0]
        y = A[n][1] - X[0][1]

        result = True
        for m in range(1, M):
            if (X[m][0] + x) not in Ax or (X[m][1] + y) not in Ay:
                result = False
                break

        if result:
            return "{} {}".format(x, y)

if __name__ == "__main__":
    _M = readInteger()
    _X = readIntegerMatrix(_M, 2)
    _N = readInteger()
    _A = readIntegerMatrix(_N, 2)

    print(main(_M, _X, _N, _A))
