""" C
    https://atcoder.jp/contests/abc173/tasks/abc173_c
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

def _pattern(N):
    if N > 1:
        pa = _pattern(N-1)
        return [[0] + p for p in pa] + [[1] + p for p in pa]
    else:
        return [[0], [1]]

def main(H, W, K, c):
    count = 0
    pwSet = _pattern(W)
    phSet = _pattern(H)
    for ph in phSet:
        result = []
        for i in range(0, len(ph)):
            if ph[i] == 1:
                result.append(c[i])
        for pw in pwSet:
            s = 0
            for r in result:
                s += sum([1 if r[j] == "#" and pw[j] == 1 else 0 for j in range(0, len(r))])
            if s == K:
                count += 1
    return count

if __name__ == "__main__":
    _H, _W, _K = readIntegerSet(3)
    _c = [list(readString().strip()) for _ in range(0, _H)]

    print(main(_H, _W, _K, _c))