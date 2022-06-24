#!/usr/bin/python3

def mySqrt(x):
    low = 0
    high = x + 1
    mid = (low + high) // 2
    while low < high:
        midSquare = mid * mid
        if midSquare == x:
            return mid
        elif midSquare < x:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2
    return mid if mid * mid < x else mid - 1

print(mySqrt(3))
print(mySqrt(4))
print(mySqrt(8))

