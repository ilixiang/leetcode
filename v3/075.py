#!/usr/bin/python3

def sortColors(nums):
    counts = [0] * 3
    for num in nums:
        counts[num] += 1
    
    i = 0
    for color in range(3):
        for j in range(counts[color]):
            nums[i] = color
            i += 1
