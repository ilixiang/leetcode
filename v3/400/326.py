#!/usr/bin/python3

def isPowerOfThree(n):
    if n <= 0:
        return False
    while n != 1 and n % 3 == 0:
        n //= 3
    return n == 1
