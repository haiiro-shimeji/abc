""" http://mtsmfm.github.io/2016/06/04/doukaku-e04.html
"""

import sys
import os
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

CONV_T = list('ABCDEFGH')

def main(paths, rock):
    """ main
    """
    rock_route = [CONV_T.index(rock)]
    rock_route_ = []

    # Rock route.
    for i in range(0, len(paths)):
        left_path = rock_route[-1] + 1
        right_path = (rock_route[-1]- 1) % 8 + 1
        if left_path == paths[i]:
            rock_route.append((rock_route[-1]+1) % 8)
            rock_route_.append(left_path)
        elif right_path == paths[i]:
            rock_route.append((rock_route[-1]-1) % 8)
            rock_route_.append(right_path)
        else:
            rock_route.append(rock_route[-1])
            rock_route_.append(-1)

    rock_route.reverse()
    rock_route_.reverse()
    paths.reverse()

    logging.debug("Rock route: {}".format(_format_route(rock_route, rock_route_)))

    reachers = []

    # Climber route.
    for c in range(0, len(CONV_T)):
        route = [c]
        route_ = []
        if route[0] == rock_route[0]:
            logging.debug(CONV_T[c] + " cannot pass.")
            continue
        for i in range(0, len(paths)):
            left_path = route[-1] + 1
            right_path = (route[-1]- 1) % 8 + 1
            if left_path == paths[i]:
                route.append((route[-1]+1) % 8)
                route_.append(left_path)
            elif right_path == paths[i]:
                route.append((route[-1]-1) % 8)
                route_.append(right_path)
            else:
                route.append(route[-1])
                route_.append(-1)
            if route_[i] != -1 and route_[i] == rock_route_[i]:
                logging.debug(CONV_T[c] + " cannot pass.")
                break
        else:
            reachers.append(CONV_T[c])
            logging.debug("{} passes: {}".format(CONV_T[c], _format_route(route, route_)))

    return "".join(reachers)

def _format_route(route, route_):
    result = CONV_T[route[0]]
    for i in range(0, len(route_)):
        result += str(route_[i]) if -1 != route_[i] else "-"
        result += CONV_T[route[i+1]]
    return result

if __name__ == "__main__":
    _S = readString()
    _paths = [int(s) for s in list(_S.split(':')[0])]
    _rock = _S.split(':')[1].rstrip()

    print(main(_paths, _rock))
