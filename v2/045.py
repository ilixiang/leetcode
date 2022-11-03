#!/usr/bin/python3

def jump(nums):
    if len(nums) == 0:
        return 0
    maxScannedIndex = 0
    position = 0
    step = 0
    while position + nums[position] < len(nums) - 1:
        nextPosition = position
        for availablePosition in range(maxScannedIndex + 1, position + nums[position] + 1):
            if nums[availablePosition] + availablePosition > nums[nextPosition] + nextPosition:
                nextPosition = availablePosition
        maxScannedIndex = position + nums[position]
        position = nextPosition
        step += 1
    return step + 1
