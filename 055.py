#!/usr/bin/python3

def canJump(nums):
    if len(nums) == 0:
        return True

    steps = 1
    remainSteps = len(nums)
    while steps < remainSteps and steps != 0:
        steps = steps - 1
        steps = max(steps, nums[len(nums) - remainSteps])
        remainSteps = remainSteps - 1
    return steps >= remainSteps

print(canJump([3,2,1,0,4]))

