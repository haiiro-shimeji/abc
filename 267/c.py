""" https://atcoder.jp/contests/abc267/tasks/abc267_c
"""
def readIntegerSet(n):
    return list(map(int, input().split(" ")[:n]))

def main(N, M, A):
    """ main
    """
    moment = sum([(j+1) * A[j] for j in range(M)])
    sum_ = sum([A[j] for j in range(M)])
    result = moment
    for i in range(1, N-M+1):
        moment = moment - sum_ + A[i+M-1] * M
        sum_ = sum_ - A[i-1] + A[i+M-1]
        result = max(result, moment)

    return result

if __name__ == "__main__":
    N, M = readIntegerSet(2)
    A = readIntegerSet(N)
    print(main(N, M, A))
