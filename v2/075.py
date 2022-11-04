#!/usr/bin/python3

def sortColors(nums):
    counts = [0, 0, 0]
    for num in nums:
        counts[num] += 1
    
    i = 0
    for color in range(0, 3):
        for count in range(0, counts[color]):
            nums[i] = color
            i += 1

    
