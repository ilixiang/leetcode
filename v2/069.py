#!/usr/bin/python3

def mySqrt(x):
    if x == 0 or x == 1:
        return x

    left = 1
    right = x + 1
    while left < right:
        mid = (left + right) // 2
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid
    return (left + right) // 2 - 1
