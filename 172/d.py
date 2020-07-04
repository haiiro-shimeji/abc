import sys
import math

def _f(x):
    result = []

    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            result.append(i)
            if int(x / i) != i:
                result.append(int(x / i))

    return result

def f(x):
    count = 0

    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            count = count + (2 if int(x / i) != i else 1)

    return count

def main(n):
    """ main
    """
    return sum([k * f(k) for k in range(1, n+1)])

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    print(main(N))