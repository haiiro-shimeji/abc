""" D
    https://atcoder.jp/contests/abc173/tasks/abc173_d
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

def main(N, A):
    A.sort(reverse=True)

    sum = A[0]
    for i in range(1, N-1):
        sum += A[int((i-1)/2)+1]

    return sum

if __name__ == "__main__":
    _N = readInteger()
    _A = readIntegerSet(_N)

    print(main(_N, _A))