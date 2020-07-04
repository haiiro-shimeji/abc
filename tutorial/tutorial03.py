""" tutorial03
    https://atcoder.jp/contests/abc122/tasks/abc122_b
"""
import sys
import math

def main(s):
    """ main
    """
    result = 0
    count = 0

    for c in s:
        if c in ["A", "T", "C", "G"]:
            count += 1
        else:
            if result < count:
                result = count
            count = 0

    if result < count:
        result = count

    return result

if __name__ == "__main__":
    S = sys.stdin.readline()

    print(main(S))