#!/usr/bin/python3

def removeDuplicates(nums):
    delimiter = 0
    i = 0
    while i < len(nums):
        if i != 0 and nums[i] == nums[i - 1]:
            i += 1
            continue
        nums[delimiter] = nums[i]
        delimiter += 1
        i += 1
    return delimiter
