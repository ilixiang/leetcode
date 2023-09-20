#!/usr/bin/python3

def guess(num):
    pass

def guessNumber(n):
    left, right = 1, n
    while left <= right:
        mid = (left + right) >> 1
        tmp = guess(mid)
        if tmp == 0:
            return mid
        elif tmp == -1:
            right = mid - 1
        else:
            left = mid + 1
    return None

