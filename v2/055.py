#!/usr/bin/python3

def canJump(nums):
    position = 0
    scannedMaxIndex = 0
    coveredIndex = nums[position]
    while coveredIndex < len(nums) - 1:
        if scannedMaxIndex == coveredIndex:
            return False
        nextPosition = scannedMaxIndex + 1
        while nextPosition <= coveredIndex:
            if nextPosition + nums[nextPosition] > position + nums[position]:
                position = nextPosition
            nextPosition += 1
        scannedMaxIndex = coveredIndex
        coveredIndex = position + nums[position]
    return True
