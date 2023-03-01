#!/usr/bin/python3

def twoSum(nums, target):
    m = {}
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num

        diffIndex = m.get(diff, None)
        if diffIndex != None:
            return [diffIndex, i]
        m[num] = i
    return None
