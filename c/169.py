""" 170/C
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
    return [lambda _: readIntegerSet(m) for _ in range(0, n)]

def main(A, B):
    B1 = int(B)
    B2 = int((100 * B) % 100)

    return int(A * B1) + int((A * B2) // 100)

if __name__ == "__main__":
    _A, _B = readStringSet(2)

    _A = int(_A)
    _B = float(_B)

    print(main(_A, _B))