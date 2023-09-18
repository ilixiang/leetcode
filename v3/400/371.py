#!/usr/bin/python3

def getSum(a, b):
    def add(x, y):
        while y != 0:
            tmp = x ^ y
            y = (x & y) << 1
            x = tmp
        return x
    def sub(x, y):
        while y != 0:
            tmp = x ^ y
            y = ((~x) & y) << 1
            x = tmp
        return x
    if a >= 0 and b >= 0:
        return add(a, b)
    elif a < 0 and b < 0:
        return -1 * add(-a, -b)
    else:
        factor = 1
        if a < b:
            a, b = b, a
        if a < -b:
            return -1 * sub(-b, a)
        else:
            return sub(a, -b)
