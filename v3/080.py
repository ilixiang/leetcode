#!/usr/bin/python3

def removeDuplicates(nums):
    l = r = delimiter = 0
    while r < len(nums):
        if nums[r] != nums[l]:
            l = r
        if r - l < 2:
            nums[delimiter] = nums[r]
            delimiter += 1
        r += 1
    return delimiter
