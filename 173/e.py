""" E
    https://atcoder.jp/contests/abc173/tasks/abc173_e
"""
import sys
import math
from functools import reduce

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

def main(N, K, A):
    A = [(abs(a), a > 0) for a in A]
    A.sort(reverse=True, key=lambda _t: _t[0])

    candidate = A[0:K]

    # if candidate is negative
    if len(list(filter(lambda _t: not _t[1], candidate)))%2:
        if candidate[K-1] < 0:
            candidate.append(A[K][0])
        else:
            if A[K+1][0] < 0:
                candidate.append(A[K+1][0])
            else:
                candidate[K-2] = A[K][0]
                candidate.append(A[K+1][0])

    result = 1
    for a in candidate:
        result = (result * a) % 1000000007
        
    return result

if __name__ == "__main__":
    _N, _K = readIntegerSet(2)
    _A = readIntegerSet(_N)

    print(main(_N, _K, _A))