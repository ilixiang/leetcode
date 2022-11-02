#!/usr/bin/python3

def twoSum(nums, target):
    m = {}
    for i in range(0, len(nums)):
        val = nums[i]
        diff = target - val
        if diff in m:
            return [m[diff], i]
        m[val] = i
    return None
