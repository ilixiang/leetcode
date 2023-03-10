#!/usr/bin/python3

def grayCode(n):
    rev = [0] * (2 ** n)
    rev[1] = 1
    for i in range(1, n):
        l, r = 2 ** i, 2 ** (i + 1)
        for j in range(l, r):
            rev[j] = (1 << i) | rev[2 * l - j - 1]
    return rev
