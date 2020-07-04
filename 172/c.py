import sys

def main(n, m, k, a, b):
    """ main
    """

    bestScore = 0
    _k = 0
    _ai = 0

    while True:
        if _ai >= n or _k + a[_ai] > k:
            bestScore = _ai
            break
        else:
            _k = _k + a[_ai]
            _ai = _ai + 1

    _bi = 0

    while _bi < m:
        _k = _k + b[_bi]

        while _k > k and _ai - 1 >= 0:
            _k = _k - a[_ai - 1] 
            _ai = _ai - 1

        if _k > k:
            break

        _bi = _bi + 1

        if _ai + _bi > bestScore:
            bestScore = _ai + _bi

    return bestScore

if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split(" "))
    A = list(map(int, sys.stdin.readline().split(" ")))
    B = list(map(int, sys.stdin.readline().split(" ")))

    print(main(N, M, K, A, B))