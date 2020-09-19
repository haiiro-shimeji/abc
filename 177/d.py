""" D
    https://atcoder.jp/contests/abc175/tasks/abc175_d
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

def main(N, K, P, C):
    best = None

    for i in range(0, N):
        s = i
        sum_c = 0
        for _ in range(0, K%N):
            i = P[i]-1
            sum_c += C[i]
            if best is None or best < sum_c:
                best = sum_c

    cycle_best = None
    for i in range(0, N):
        s = i
        sum_c = 0
        for _ in range(0, N):
            i = P[i]-1
            sum_c += C[i]
        if cycle_best is None or cycle_best < sum_c:
            cycle_best = sum_c

    print(best, cycle_best)

    if cycle_best > 0:
        best += cycle_best * ((K-1) // N)

    return best

if __name__ == "__main__":
    _N, _K = readIntegerSet(2)
    _P = readIntegerSet(_N)
    _C = readIntegerSet(_N)

    print(main(_N, _K, _P, _C))