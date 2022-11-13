#!/usr/bin/python3

def moveZero(nums):
    divider = 0
    for i in range(0, len(nums)):
        num = nums[i]
        if num != 0:
            nums[divider] = nums[i]
            divider += 1
    
    for i in range(divider, len(nums)):
        nums[i] = 0
