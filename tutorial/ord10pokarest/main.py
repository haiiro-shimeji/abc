""" http://nabetani.sakura.ne.jp/hena/ord10pokarest/
"""
import os
import sys
import re
import logging

logging.getLogger().setLevel(int(os.getenv('LOG_LEVEL', 40)))

RANK = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']

def _calc_hand(cards):
    if _is_FL(cards) and _is_royal(cards):
        return "RF"
    elif _is_FL(cards) and _is_ST(cards):
        return "SF"
    elif _is_FL(cards):
        return "FL"
    elif _is_ST(cards):
        return "ST"
    else:
        _subsets = _fetch_4_cards(cards)
        for _cards in _subsets:
            if _is_ST(_cards) and _is_FL(_cards):
                return "4SF"
        for _cards in _subsets:
            if _is_FL(_cards):
                return "4F"
        for _cards in _subsets:
            if _is_ST(_cards):
                return "4S"

    return "-"

def _split_cards(_s):
    return re.finditer(r'(\d+|[JQKA])[scdh]', _s)

def _is_FL(_cards):
    suit = _cards[0][-1]
    return all([
        suit == _c[-1]
        for i, _c in enumerate(_cards[1:])
    ])

def _is_ST(_cards):
    def _f(_cards):
        _cards = sorted(_cards, key=lambda s: RANK.index(s[:-1]))
        _first = RANK.index(_cards[0][:-1])
        return all([
            _first+i+1 == RANK.index(_c[:-1])
            for i, _c in enumerate(_cards[1:])
        ])

    return _f(_cards) or _f(_convert_A_to_1(_cards))

def _is_royal(_cards):
    _cards = sorted(_cards, key=lambda s: RANK.index(s[:-1]))
    return _cards[0][:-1] == '10' \
        and _cards[1][:-1] == 'J' \
        and _cards[2][:-1] == 'Q' \
        and _cards[3][:-1] == 'K' \
        and _cards[4][:-1] == 'A'

def _convert_A_to_1(_cards):
    return [_c.replace('A', '1') for _c in _cards]

def _fetch_4_cards(_cards):
    return [_cards[0:i] + _cards[i+1:] for i in range(5)]

def _main(_S):
    cards = [m.group(0) for m in _split_cards(_S.rstrip())]

    logging.debug(cards)

    return _calc_hand(cards)

if __name__ == "__main__":
    print(_main(sys.stdin.readline()))
