""" C
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
    M = pow(10, 9) + 7
    result = 0
    S = sum(A)
    for i in range(len(A)):
        S = S - A[i]
        result = (result + A[i] * S) % M
    return result

if __name__ == "__main__":
    _N = readInteger()
    _A = readIntegerSet(_N)

    print(main(_N, _A))