#!/usr/bin/python3

def canJump(nums):
    reached = -1
    reachable = 0
    while reachable < len(nums) - 1 and reached < reachable:
        tmp = reachable
        for i in range(reached + 1, reachable + 1):
            reachable = max(reachable, i + nums[i])
        reached = tmp
    return reachable >= len(nums) - 1
