""" https://atcoder.jp/contests/abc267/tasks/abc267_a
"""

def readString():
    return input()

def main(S):
    """ main
    """
    l = ['', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', ]
    return l.index(S)

if __name__ == "__main__":
    S = readString()
    print(main(S))
