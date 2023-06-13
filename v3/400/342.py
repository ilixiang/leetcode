#!/usr/bin/python3

def isPowerOfFour(n):
    if n == 0:
        return False
    while n != 1 and n & 3 == 0:
        n >>= 2
    return n == 1
