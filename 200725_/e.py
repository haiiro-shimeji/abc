""" E
    https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_e
"""
import sys
import math
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
    return [readIntegerSet(m) for _ in range(0, n)]

def main(N, M):
    line_x = [0]
    line_y = [0]

    print(sum(
        [
            min([abs(x - x_) for x_ in line_x] 
            + [abs(y - y_) for y_ in line_y]) * p 
            for x, y, p in M
        ]
    ))

    for _ in range(1, N+1):
        bestScore = math.inf
        ax = ay = None
        for cx, cy, _ in M:
            print("cx=", cx,
                    [
                        [abs(x - x_) for x_ in line_x+[cx]] 
                        + [abs(y - y_) for y_ in line_y]
                        for x, y, p in M
                    ]
                )
            Sx = sum(
                    [
                        min([abs(x - x_) for x_ in line_x+[cx]] 
                        + [abs(y - y_) for y_ in line_y]) * p 
                        for x, y, p in M
                    ]
                )
            Sy= sum(
                    [
                        min([abs(x - x_) for x_ in line_x] 
                        + [abs(y - y_) for y_ in line_y+[cy]]) * p 
                        for x, y, p in M
                    ]
                )
            print(cx, Sx, cy, Sy)
            if bestScore > Sx:
                bestScore = Sx
                ax = cx
                ay = None
            if bestScore > Sy:
                bestScore = Sy
                ay = cy
                ax = None

        if ax is not None:
            line_x.append(cx)
        if ay is not None:
            line_y.append(cy)

        print(bestScore)

if __name__ == "__main__":
    _N = readInteger()
    _M = readIntegerMatrix(_N, 3)

    main(_N, _M)