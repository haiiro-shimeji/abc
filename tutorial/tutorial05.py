""" tutorial05
    https://atcoder.jp/contests/abc095/tasks/arc096_a
"""
import sys
import math
from functools import reduce

def readStringSet(n):
    return sys.stdin.readline().split(" ")[:n]

def readIntegerSet(n):
    return list(map(int, readStringSet(n)))

def main(A, B, C, X, Y):
    """ main
    """
    if A + B > 2 * C:
        result = min([X, Y]) * 2 * C

        if X > Y:
            if A > 2 * C:
                return result + (X - Y) * 2 * C
            else:
                return result + (X - Y) * A
        else:
            if B > 2 * C:
                return result + (Y - X) * 2 * C
            else:
                return result + (Y - X) * B
    else:
        return X * A + Y * B

if __name__ == "__main__":
    _A, _B, _C, _X, _Y = readIntegerSet(5)

    print(main(_A, _B, _C, _X, _Y))