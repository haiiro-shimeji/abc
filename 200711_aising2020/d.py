""" D
    https://atcoder.jp/contests/aising2020/tasks/aising2020_d
"""
import sys
import math
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

def div_by(n, x, k):
    result = 0
    for i in n:
        if x[i] == "1":
            result = (result + pow(2, n-i-1)) % k
    return result

def popcount(x):
    return sum([int(c) for c in x])

def main(N, X):
    for i in range(0, N):
        X_ = X[0:i] + ('1' if X[i] == '0' else '0') + X[i+1:]
        x = int(X_, 2)
        count = 0
        while x > 0:
            k = popcount(x)
            x = x % k
            count += 1
        print(count)

if __name__ == "__main__":
    _N = readInteger()
    _X = readString()

    main(_N, _X)