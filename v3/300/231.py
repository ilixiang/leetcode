#!/usr/bin/python3

def isPowerOfTwo(n):
    for i in range(32):
        num = 1 << i
        if num == n:
            return True
        elif num > n:
            return False
    return False
