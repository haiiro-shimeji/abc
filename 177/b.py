""" B
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
    return [readIntegerSet(m) for _ in range(0, n)]

def main(T, S):
    best = sys.maxsize
    for i in range(len(T)-len(S)+1):
        s = T[i:i+len(S)]
        count = 0
        for j in range(len(S)):
            if s[j] != S[j]:
                count += 1
        if best > count:
            best = count
    return best


if __name__ == "__main__":
    _T = readString().rstrip()
    _S = readString().rstrip()

    print(main(_T, _S))
