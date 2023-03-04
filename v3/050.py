#!/usr/bin/python3

def myPow(x, n):
    if n == 0:
        return float(1)
    
    if n == 1:
        return x
    
    if n < 0:
        return 1 / myPow(x, -1 * n)
    
    if n & 1 == 0:
        tmp = myPow(x, n >> 1)
        return tmp * tmp
    else:
        tmp = myPow(x, n >> 1)
        return tmp * tmp * x
