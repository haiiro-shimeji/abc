""" http://nabetani.sakura.ne.jp/hena/ord9busfare/
"""
import os
import sys
import math
from functools import reduce
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

def _calc_fee(default_fee, m):
    fee = default_fee if m.startswith('A') \
        else math.ceil(default_fee / 2 / 10) * 10

    return int(
        0 if m.endswith('p') \
        else math.ceil(fee / 2 / 10) * 10 if m.endswith('w') \
        else fee
    )

def _group(fees):
    result = {
        "A": [],
        "C": [],
        "I": [],
    }

    for m, f in fees:
        if m.startswith('A'):
            result['A'].append(f)
        if m.startswith('C'):
            result['C'].append(f)
        if m.startswith('I'):
            result['I'].append(f)

    return result

def main(default_fee, members):
    logging.debug([default_fee, members])

    # 各メンバーの料金を計算する
    fees = _group([(m, _calc_fee(default_fee, m)) for m in members])

    logging.debug(fees)

    # 幼児料金を高い方から無料にするため並べ替え.
    fees['I'].sort(reverse=True)

    # 幼児の料金を大人の人数x2ぶん無料に変える
    for i in range(0, min(len(fees["A"]) * 2, len(fees["I"]))):
        fees["I"][i] = 0

    # 合計算出
    return sum([sum(a) for a in fees.values()])

if __name__ == "__main__":
    _S = readString()
    _fee = int(_S.split(':')[0].rstrip())
    _members = _S.split(':')[1].rstrip().split(',')

    print(main(_fee, _members))
