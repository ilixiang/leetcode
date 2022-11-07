#!/usr/bin/python3

def reverseBits(n):
    rev = 0
    for i in range(0, 32):
        if i <= 15:
            rev |= (n & (1 << i)) << (31 - i * 2)
        else:
            rev |= (n & (1 << i)) >> (i * 2 - 31)
    return rev
