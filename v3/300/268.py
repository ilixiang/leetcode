#!/usr/bin/python3

def missingNumber(nums):
    n = len(nums)
    return (n + 1) * n // 2 - sum(nums)
