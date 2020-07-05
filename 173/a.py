""" A
    https://atcoder.jp/contests/abc173/tasks/abc173_a
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
    return (1000 - (N%1000))%1000

if __name__ == "__main__":
    _N = readInteger()

    print(main(_N))