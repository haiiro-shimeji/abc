import sys
from functools import reduce

def _main():
    s = sys.stdin.readline()
    t = sys.stdin.readline()

    print(reduce(lambda acc, _t: acc + (1 if _t[0] != _t[1] else 0), zip(s, t), 0))

if __name__ == "__main__":
    _main()