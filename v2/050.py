#!/usr/bin/python3

def myPow(x, n):
    if n < 0:
        return 1 / myPow(x, -1 * n)

    if n == 0:
        return 1

    if n == 1:
        return x
    
    tmp = myPow(x, n >> 1)
    return tmp * tmp * (x if n & 1 == 1 else 1)

