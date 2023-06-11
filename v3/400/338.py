#!/usr/bin/python3

def countBits(n):
    rev = [0] * (n + 1)
    i = 1
    while i <= n:
        j = 0
        while j < i and i + j <= n:
            rev[i + j] = rev[j] + 1
            j += 1
        i *= 2
    return rev
