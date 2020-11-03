""" C
"""
import sys
import math
from functools import reduce
from bisect import bisect_left

def readString():
    return sys.stdin.readline()

def readInteger():
    return int(readString())

def readStringSet(n):
    return sys.stdin.readline().split(" ")[:n]

def readIntegerSet(n):
    return list(map(int, readStringSet(n)))

def readIntegerMatrix(n, m):
    return reduce(lambda acc, _: acc + [readIntegerSet(m)], range(0, n), [])

def _break(AB):
    result = [1]
    n = 2
    while n < AB+1:
        while (AB / n).is_integer():
            AB = int(AB/n)
            result.append(n)

        if AB == 1:
            break

        n += 1

    return result

def main(N, M, AB):
    groups = []
    vs = {}

    for A, B in AB:
        g_has_A = [i for i in range(len(groups)) if A in groups[i]]
        g_has_B = [i for i in range(len(groups)) if B in groups[i]]

        # AもBも持つgroupがあったら、なにもしない
        if len(g_has_A) == 1 and len(g_has_B) == 1 \
            and g_has_A[0] == g_has_B[0]:
            pass
        # Aを持つgroupとBを持つグループが分かれていたら、連結する
        elif len(g_has_A) == 1 and len(g_has_B) == 1 \
            and g_has_A[0] != g_has_B[0]:
            groups[g_has_A[0]] += groups[g_has_B[0]]
            groups.pop(g_has_B[0])
        # 片方を持つgroupだけがあった場合は、そこにもう一方を加える
        elif len(g_has_A) == 1:
            groups[g_has_A[0]][B] = B
        elif len(g_has_B) == 1:
            groups[g_has_B[0]][A] = A
        # どちらも既存groupになければ、groupを加える
        else:
            groups.append({A:A, B:B})

        vs[A] = A
        vs[B] = B

    return len(groups) + (N-len(vs.keys())) -1

if __name__ == "__main__":
    _N, _M = readIntegerSet(2)
    _AB = readIntegerMatrix(_M, 2)

    print(main(_N, _M, _AB))