""" F
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

def readIntegerMatrix_(n, m):
    for _ in range(0, n):
        yield readIntegerSet(m)

def main(H, W, M):
    c = 0
    A, B = next(M)
    x = 0 if A > 1 else B

    for k in range(H):
        if k > 0:
            A, B = next(M)
        if x > W-1:
            print(-1)
            continue
        if x >= A-1 and x <= B-1:
            x0 = x
            x = B
            if x > W-1:
                print(-1)
                continue
            c += (x - x0 + 1)
        else:
            c += 1
        print(c)

if __name__ == "__main__":
    _H, _W = readIntegerSet(2)
    _M = readIntegerMatrix_(_H, 2)

    main(_H, _W, _M)