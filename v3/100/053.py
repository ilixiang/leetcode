#!/usr/bin/python3

def maxSubArray(nums):
    rev = nums[0]
    prevMax = 0
    for i in range(len(nums)):
        prevMax = nums[i] if prevMax <= 0 else prevMax + nums[i]
        rev = max(rev, prevMax)
    return rev
