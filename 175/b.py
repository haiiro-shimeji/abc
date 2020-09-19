""" B
    https://atcoder.jp/contests/abc175/tasks/abc175_b
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

def main(N, L):
    count = 0

    for i in range(0, N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                lines = [L[i], L[j], L[k]]
                if L[i] == L[j] or L[j] == L[k] or L[i] == L[k]:
                    continue
                max_line = max(lines)
                sum_line = sum(lines) 
                if max_line < sum_line - max_line:
                    count += 1

    return count

if __name__ == "__main__":
    _N = readInteger()
    _L = readIntegerSet(_N)

    print(main(_N, _L))
