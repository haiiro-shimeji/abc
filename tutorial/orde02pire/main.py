""" http://nabetani.sakura.ne.jp/hena/orde02pire/
"""
import os
import sys
import math
from functools import reduce
from itertools import groupby
import logging

logging.getLogger().setLevel(int(os.getenv('LOG_LEVEL', 40)))

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

def _coords(code):
    def _coord(c):
        if '0' <= c and '9' >= c:
            return ord(c) - ord('0')
        elif 'A' <= c and 'Z' >= c:
            return ord(c) - ord('A') + 10
        else:# 'a' <= c and 'z' >= c:
            return ord(c) - ord('a') + 36

    return (_coord(code[0]), _coord(code[1]))

def _closed_ranges(a):
    sorted_a = sorted(a)
    for i in range(len(sorted_a)):
        for j in range(i, len(sorted_a)):
            yield (sorted_a[i], sorted_a[j]+1)

def _opened_ranges(a):
    sorted_a = sorted(a)
    sorted_a = [-1] + sorted_a + [62]

    for i in range(len(sorted_a)):
        for j in range(i+1, len(sorted_a)):
            yield (sorted_a[i]+1, sorted_a[j])

def _main(_S):
    N = int(_S.split(':')[0])
    dots = [_coords(code) for code in _S.split(':')[1].split(',')]

    logging.debug([N, dots])

    min_value = 62 * 62 + 1
    max_value = -1

    # 最小
    x_ranges = list(_closed_ranges([x for x, y in dots]))
    y_ranges = list(_closed_ranges([y for x, y in dots]))
    for x0, x1 in x_ranges:
        for y0, y1 in y_ranges:
            # この四角に入っている点の数
            n = len([(x, y) for x, y in dots if x0 <= x and x < x1 and y0 <= y and y < y1])
            if N == n:
                value = (x1 - x0) * (y1 - y0)
                if value < min_value:
                    logging.debug('min cand: {}: {}'.format(n, [x0, x1, y0, y1]))
                    min_value = value

    # 最大
    x_ranges = list(_opened_ranges([x for x, y in dots]))
    y_ranges = list(_opened_ranges([y for x, y in dots]))
    for x0, x1 in x_ranges:
        for y0, y1 in y_ranges:
            # この四角に入っている点の数
            n = len([(x, y) for x, y in dots if x0 <= x and x < x1 and y0 <= y and y < y1])
            if N == n:
                value = (x1 - x0) * (y1 - y0)
                if value > max_value:
                    logging.debug('max cand: {}: {}'.format(n, [x0, x1, y0, y1]))
                    max_value = value

    return '{},{}'.format(min_value, max_value) \
            if min_value < 62 * 62 + 1 and max_value > -1 else '-'

if __name__ == "__main__":
    print(_main(readString()))
