""" https://atcoder.jp/contests/abc257/tasks/abc257_a
"""

def readIntegerSet(n):
    return list(map(int, input().split(" ")[:n]))

def main(N, X):
    """ main
    """
    return chr(65 + (X-1) // N)

if __name__ == "__main__":
    N, X = readIntegerSet(2)
    print(main(N, X))
