#!/usr/bin/python3

def missingNumber(nums):
    n = len(nums)
    s = n * (n + 1) // 2
    r = s
    for num in nums:
        r = r - num
    return r

