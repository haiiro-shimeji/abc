import sys
from functools import reduce

def main(n, k, p):
    """ main
    """
    p.sort()
    return sum(p[0:k])

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split(" "))
    P = list(map(int, sys.stdin.readline().split(" ")))

    print(main(N, K, P))