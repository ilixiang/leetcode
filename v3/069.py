#!/usr/bin/python3

def mySqrt(x):
    if x == 0 or x == 1:
        return x
    
    rev = 0
    l, r = 1, x // 2
    while l <= r:
        m = (l + r) >> 1
        p = m * m
        if p == x:
            return m
        elif p < x:
            l = m + 1
            rev = m
        else:
            r = m - 1
    return rev

