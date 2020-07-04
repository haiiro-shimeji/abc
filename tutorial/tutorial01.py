""" tutorial01
    http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja
"""
import sys

def main(n, x):
    """ main
    """
    count = 0
    i = max([1, x - n - n - 1])
    while 3 * i + 2 <= x:
        j = max([i + 1, x - i - n])
        while i + 2 * j + 1 <= x:
            count = count + 1
            j = j + 1
        i = i + 1

    return count

if __name__ == "__main__":
    while True:
        N, X = list(map(int, sys.stdin.readline().split(" ")))

        if N==0 and X==0:
            break

        print(main(N, X))