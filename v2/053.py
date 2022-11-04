#!/usr/bin/python3

def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    
    prevMax = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        prevMax = nums[i] if prevMax <= 0 else prevMax + nums[i]
        res = max(res, prevMax)
    return res
