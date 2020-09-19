""" A
    https://atcoder.jp/contests/aising2020/tasks/aising2020_a
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

def main(L, R, d):
    count = 0
    for i in range(L, R+1):
        if i % d == 0:
            count += 1
    return count

if __name__ == "__main__":
    _L, _R, _d = readIntegerSet(3)

    print(main(_L, _R, _d))