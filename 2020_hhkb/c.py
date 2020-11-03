""" C
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

def _break(AB):
    result = [1]
    n = 2
    while n < AB+1:
        while (AB / n).is_integer():
            AB = int(AB/n)
            result.append(n)

        if AB == 1:
            break

        n += 1

    return result

def main(N, P):
    used = {}
    min = 0
    for i in range(N):
        used[P[i]] = P[i]
        if P[i] == min:
            while min in used:
                min += 1

        print(min)

if __name__ == "__main__":
    _N = readInteger()
    _P = readIntegerSet(_N)

    main(_N, _P)