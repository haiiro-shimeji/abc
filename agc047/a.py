""" A
    https://atcoder.jp/contests/agc047/tasks/agc047_a
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

def main(N, A):
    count = 0

    p9 = pow(10, 9)
    p18 = pow(10, 18)

    for i in range(0, _N):
        for j in range(i+1, _N):
            Ai_0 = int(A[i])
            Ai_1 = int(A[i] * p9) % p9
            Aj_0 = int(A[j])
            Aj_1 = int(A[j] * p9) % p9

            C = (
                (Ai_0 * Aj_1) % p9 * p9 \
                + (Aj_0 * Ai_1) % p9 * p9 \
                + (Ai_1 * Aj_1) % p18
            ) % p18

            if C == 0:
                count += 1

    return count

if __name__ == "__main__":
    _N = readInteger()
    _A = [float(readString()) for _ in range(0, _N)]

    print(main(_N, _A))