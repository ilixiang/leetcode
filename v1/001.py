#!/usr/bin/python3

def twoSum(nums, target):
    m = {}
    for i in range(0, len(nums)):
        num = nums[i]
        diff = target - num
        if m.get(diff) != None:
            return [m[diff], i]
        m[num] = i
    return []

print(twoSum([2, 7, 11, 15], 9))
