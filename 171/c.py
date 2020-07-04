import sys

def main(n):
    """ main
    """
    result = []

    n = n - 1

    while True:
        result.append(chr(97 + n%26))
        n = int(n / 26) - 1

        if n < 0:
            break

    result.reverse()

    return "".join(result)

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    print(main(N))