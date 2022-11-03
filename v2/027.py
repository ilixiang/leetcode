#!/usr/bin/python3

def removeElement(nums, val):
    delimiter = 0
    i = 0
    while i < len(nums):
        if nums[i] != val:
            nums[delimiter] = nums[i]
            delimiter += 1
        i += 1
    return delimiter
