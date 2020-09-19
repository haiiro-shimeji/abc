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

def main(N, S):
    S = list(S.rstrip())

    cr = len([c for c in S if "R" == c])
    cw = len([c for c in S if "W" == c])

    if cw < abs(cr-cw) or cr < abs(cr-cw):
        return min(cw, cr-1)



    if len([c for c in S if "W" == c]) == 0:
        return 0

    return len([c for c in S[len(S)//2:] if "R" == c])

if __name__ == "__main__":
    _N = readInteger()
    _S = readString()

    print(main(_N, _S))