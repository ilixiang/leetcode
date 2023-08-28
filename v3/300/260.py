#!/usr/bin/python3

def singleNumber(nums):
    xorNum = 0
    for num in nums:
        xorNum ^= num

    mask = xorNum & (-xorNum)
    
    rev = [0, 0]
    for num in nums:
        idx = 0 if (num & mask) == 0 else 1
        rev[idx] ^= num
    return rev

