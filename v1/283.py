#!/usr/bin/python3

def moveZeroes(nums):
    d = -1
    length = len(nums)
    for i in range(length):
        if nums[i] != 0:
            nums[d + 1] = nums[i]
            d += 1

    d += 1
    while d < length:
        nums[d] = 0
        d += 1


