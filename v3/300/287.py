#!/usr/bin/python3

def findDuplicate(nums):
    s, f = nums[0], nums[nums[0]]
    while s != f:
        s = nums[s]
        f = nums[nums[f]]
    s = 0
    while s != f:
        s = nums[s]
        f = nums[f]
    return s
