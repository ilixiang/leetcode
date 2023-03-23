#!/usr/bin/python3

def singleNumber(nums):
    rev = 0
    for num in nums:
        rev ^= num
    return rev
