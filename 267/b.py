""" https://atcoder.jp/contests/abc267/tasks/abc267_b
"""

def readString():
    return input()

def main(S):
    """ main
    """
    if S[0] != '0':
        return 'No'

    C = [
        S[6] == '1',
        S[3] == '1',
        S[7] == '1' or S[1] == '1',
        S[4] == '1',
        S[8] == '1' or S[2] == '1',
        S[5] == '1',
        S[9] == '1'
    ]

    B = [_i for _i, c in enumerate(C) if c == True]

    for _i in range(len(B)-1):
        if B[_i+1] - B[_i] > 1:
            return 'Yes'

    return 'No'

if __name__ == "__main__":
    S = readString()
    print(main(S))
