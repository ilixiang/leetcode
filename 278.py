#!/usr/bin/python3

def firstBadVersion(n):
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    mid = (left + right) // 2
    return mid

