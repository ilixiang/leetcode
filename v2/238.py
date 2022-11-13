#!/usr/bin/python3

def productExceptSelf(nums):
    product = 1
    zeroCount = 0
    zeroIndex = -1
    for i in range(0, len(nums)):
        num = nums[i]
        if num == 0:
            zeroCount += 1
            zeroIndex = i
        else:
            product *= num
    
    rev = [0] * len(nums)
    if zeroCount >= 2:
        return rev
    elif zeroCount == 1:
        rev[zeroIndex] = product
    else:
        for i in range(0, len(nums)):
            rev[i] = product // nums[i]
    return rev
