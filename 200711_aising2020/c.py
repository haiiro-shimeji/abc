""" C
    https://atcoder.jp/contests/aising2020/tasks/aising2020_c
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

def main(N):
    maxi = int(math.sqrt(N))
    result = dict()
    for x in range(1, maxi+1):
        for y in range(1, maxi+1):
            for z in range(1, maxi+1):
                n = pow(x, 2) + pow(y, 2) + pow(z, 2) + x*y + y*z + z*x
                if n not in result.keys():
                    result[n] = 1
                else:
                    result[n] += 1

    for n in range(1, N+1):
        if n in result.keys():
            print(result[n])
        else:
            print(0)

if __name__ == "__main__":
    _N = readInteger()

    main(_N)