""" https://atcoder.jp/contests/abc257/tasks/abc257_b
"""

def readIntergerSet(n):
    return list(map(int, input().split(" ")[:n]))

def main(N, A, L):
    B = [0] * N

    for a in A:
        B[a-1] = 1

    for l in L:
        if not stop_to_right(N, A[l-1]) \
            and not stop_to_other(B, A[l-1]):
            B[A[l-1]-1] = 0
            A[l-1] += 1
            B[A[l-1]-1] = 1

    return " ".join([str(i+1) for i in range(N) if B[i]])

def stop_to_right(N, a):
    return a == N

def stop_to_other(B, a):
    return B[a]

if __name__ == "__main__":
    N, K, Q = readIntergerSet(3)
    A = readIntergerSet(K)
    L = readIntergerSet(Q)

    print(main(N, A, L))
