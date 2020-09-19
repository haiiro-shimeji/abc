""" B
    https://atcoder.jp/contests/aising2020/tasks/aising2020_b
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

def main(N, a):
    count = 0
    for i in range(0, N):
        if (i+1)%2==1 and a[i]%2==1:
            count += 1
    return count

if __name__ == "__main__":
    _N = readInteger()
    _a = readIntegerSet(_N)

    print(main(_N, _a))