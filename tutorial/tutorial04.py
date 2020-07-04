""" tutorial04
    https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
"""
import sys
from functools import reduce

def readStringSet(n):
    return sys.stdin.readline().split(" ")[:n]

def readIntegerSet(n):
    return list(map(int, readStringSet(n)))

def readIntegerMatrix(n, m):
    return reduce(lambda acc, _: acc + [readIntegerSet(m)], range(0, n), [])

def main(n, m, a):
    """ main
    """
    _at = [list(x) for x in zip(*a)]

    bestScore = 0

    for t1 in range(0, m):
        for t2 in range(t1+1, m):
            score = sum([max(a_t1, a_t2) for a_t1, a_t2 in zip(_at[t1], _at[t2])])
            if bestScore < score:
                bestScore = score

    return bestScore

if __name__ == "__main__":
    N, M = readIntegerSet(2)
    A = readIntegerMatrix(N, M)

    print(main(N, M, A))