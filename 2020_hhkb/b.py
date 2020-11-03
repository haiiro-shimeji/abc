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

def main(H, W, S):
    count = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                if j+1 < W and S[i][j+1] == ".":
                    count += 1
                if i+1 < H and S[i+1][j] == ".":
                    count += 1
    return count


if __name__ == "__main__":
    _H, _W = readIntegerSet(2)
    _S = [readString().rstrip() for _ in range(_H)]

    print(main(_H, _W, _S))
