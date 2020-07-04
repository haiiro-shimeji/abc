""" tutorial02
    https://atcoder.jp/contests/abc106/tasks/abc106_b
"""
import sys
import math

def f(n):
    count = 0
    for j in range(1, int(math.sqrt(n)+1)):
        if n % j == 0:
            count = count + (2 if n / j != j else 1)
            if count > 8:
                break

    return count

def main(n):
    """ main
    """
    result = 0

    for i in range(1, n+1):
        if i % 2 == 1 and 8 == f(i):
            result = result + 1

    return result

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    print(main(N))