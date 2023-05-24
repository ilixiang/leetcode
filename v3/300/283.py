#!/usr/bin/python3

def moveZeroes(nums):
    i = delimiter = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[delimiter] = nums[i]
            delimiter += 1
        i += 1
    while delimiter < len(nums):
        nums[delimiter] = 0
        delimiter += 1
