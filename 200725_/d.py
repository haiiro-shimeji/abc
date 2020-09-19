""" D
    https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_d
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

def main(N, A):
    kabu = 0
    money = 1000
    for i in range(1, N):
        if A[i-1] < A[i]:
            kabu += money // A[i-1]
            money %= A[i-1]
        else:
            money += A[i-1] * kabu
            kabu = 0

    money += A[N-1] * kabu

    return money

if __name__ == "__main__":
    _N = readInteger()
    _A = readIntegerSet(_N)

    print(main(_N, _A))