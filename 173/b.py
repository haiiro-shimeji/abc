""" B
    https://atcoder.jp/contests/abc173/tasks/abc173_b
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

def main(N, S):
    result = {
        "AC": 0,
        "WA": 0,
        "TLE": 0,
        "RE": 0
    }

    for s in S:
        result[s] += 1

    print("AC x {}".format(result["AC"]))
    print("WA x {}".format(result["WA"]))
    print("TLE x {}".format(result["TLE"]))
    print("RE x {}".format(result["RE"]))

if __name__ == "__main__":
    _N = readInteger()
    _S = [readString().strip() for _ in range(0, _N)]

    main(_N, _S)