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

def main(N, X, M):
    A = X
    m = {A: A}
    i = -1
    for _ in range(1, M):
        A = (A * A) % M if M > 0 else 0
        if A in m:
            i = list(m.keys()).index(A)
            break
        else:
            m[A] = A

    if i == -1:
        return sum(m.values())
    else:
        l = list(m.values())
        s1 = sum(l[:i])
        len_repeat = len(l) - i
        s2 = sum(l[i:])

        return s1 + int((N-i)/len_repeat) * s2 + sum(l[i:(N-i)%len_repeat+i])

if __name__ == "__main__":
    _N, _X, _M = readIntegerSet(3)

    print(main(_N, _X, _M))