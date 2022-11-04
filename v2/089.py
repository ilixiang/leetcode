#!/usr/bin/python3

def grayCode(n):
    if n == 1:
        return [0, 1]
    
    size = 2 ** n
    rev = [0] * size
    rev[1] = 1
    for i in range(2, n + 1):
        left = 0
        right = 2 ** i - 1
        while left < right:
            rev[right] = rev[left] | (1 << (i - 1))
            right -= 1
            left += 1
    return rev
