""" tutorial06
    https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
"""
import sys
import math
from functools import reduce

def readString():
    return sys.stdin.readline()

def readInteger():
    return int(readString())

def main(N, S):
    """ main
    """
    count = 0
    skip1 = []
    skip2 = []
    skip3 = []

    for i in range(0, N):
        if S[i] in skip1:
            continue
        skip1.append(S[i])
        for j in range(i+1, N):
            if S[j] in skip2:
                continue
            skip2.append(S[j])
            for k in range(j+1, N):
                if S[k] in skip3:
                    continue
                skip3.append(S[k])
                count += 1
            skip3 = []
        skip2 = []

    return count

if __name__ == "__main__":
    _N = readInteger()
    _S = readString()

    print(main(_N, _S))