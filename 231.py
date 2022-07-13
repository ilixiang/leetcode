#!/usr/bin/python3

def isPowerOfTwo(n):
    if n <= 0:
        return False
    quotient = n
    while quotient != 1:
        if (quotient & 1) == 1:
            return False
        quotient = quotient >> 1
    return True


