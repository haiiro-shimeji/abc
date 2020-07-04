""" tutorial07
    https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_c
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

def _createModel(M):

    model1 = dict()
    for i in range(0, len(M)):
        if M[i][0] not in model1.keys():
            model1[M[i][0]] = []

        model1[M[i][0]].append(M[i][1])

    model2 = sorted([(k, sorted(model1[k])) for k in model1.keys()], key=lambda _t: _t[0])

    return ([_t[0] for _t in model2], [_t[1] for _t in model2])

def _inModel(model, p):
    keys, m = model

    i = bisect_left(keys, p[0])

    if i >= len(keys) or keys[i] != p[0]:
        return False

    j = bisect_left(m[i], p[1])

    return j < len(m[i]) and m[i][j] == p[1]

def main(N, M):
    """ main
    """
    model = _createModel(M)

    bestScore = 0

    count = 0

    for i in range(0, len(M)):
        for j in range(i+1, len(M)):
            score = math.pow(M[i][0] - M[j][0], 2) + math.pow(M[i][1] - M[j][1], 2)
            if bestScore >= score:
                continue

            p0 = [M[i][0], M[i][1]]
            p1 = [M[j][0], M[j][1]]
            p2 = [p1[0] - p0[1] + p1[1], p1[1] + p0[0] - p1[0]]
            p3 = [p2[0] - p1[1] + p2[1], p2[1] + p1[0] - p2[0]]

            #if p2 in M and p3 in M:
            if _inModel(model, p2) and _inModel(model, p3):
                bestScore = score
                count += 1

    print(count)

    return int(bestScore)

if __name__ == "__main__":
    _N = readInteger()
    _M = readIntegerMatrix(_N, 2)

    print(main(_N, _M))