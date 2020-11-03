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

def _P(n, m):
    ret = 1
    for i in range(m):
        ret *= n
        n -= 1
        m -= m
    return ret

def main(S):
    s = S
    ret = 0
    while s > 2:
        s -= 3
    

if __name__ == "__main__":
    _S = readInteger()

    print(main(_S))