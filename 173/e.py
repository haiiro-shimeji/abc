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

def last(a, op):
    for i in range(len(a)-1, -1):
        if op(a[i]):
            return i
    return -1

def first(a, op):
    for i in range(0, len(a)):
        if op(a[i]):
            return i
    return -1

def main(N, K, A):
    A = [(abs(a), a, a > 0) for a in A]
    A.sort(reverse=True, key=lambda _t: _t[0])

    candidate = A[0:K]

    # if candidate is negative
    if len(list(filter(lambda _t: not _t[2], candidate)))%2:
        # 候補の最小負値を残りの最大正値で代える
        i10 = last(candidate, lambda _t: not _t[2])
        i11 = first(A[K:], lambda _t: _t[2])
        impact1 = - i11 / i10 if i10 != -1 and i11 != -1 else 0

        # 候補の最小正値を残りの最大負値で代える
        i20 = last(candidate, lambda _t: _t[2])
        i21 = first(A[K:], lambda _t: not _t[2])
        impact2 = - i21 / i20 if i20 != -1 and i21 != -1 else 0

        if 0 < impact1 or 0 < impact2:
            # おおきくなれる方を採用
            if impact1 > impact2:
                candidate[i10] = A[K+i11]
            else:
                candidate[i20] = A[K+i21]
        else:
            # 負値を解消するすべがないので、仕方なく最大の負値を採る.
            candidate = A[N-K:]

    result = 1
    for _t in candidate:
        result = result * _t[1]
        if result > 1000000006 or result < 0:
            result %= 1000000007
        
    return result

if __name__ == "__main__":
    _N, _K = readIntegerSet(2)
    _A = readIntegerSet(_N)

    print(main(_N, _K, _A))