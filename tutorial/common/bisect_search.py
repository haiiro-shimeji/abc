from bisect import bisect_left

def create_model(a):
     _m = sorted([(i, a[i]) for i in range(0, len(a))], key=lambda _t: _t[1])
     return ([_t[0] for _t in _m], [_t[1] for _t in _m])

def search(e, m):
    i = bisect_left(m[1], e)
    return m[0][i] if i < len(m[1]) and m[1][i] == e else -1