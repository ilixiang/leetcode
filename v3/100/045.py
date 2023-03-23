#!/usr/bin/python3

def jump(nums):
    reached = -1
    rev = reachable = 0
    while reachable < len(nums) - 1:
        tmp = reachable
        for i in range(reached + 1, reachable + 1):
            reachable = max(reachable, i + nums[i])
        reached = tmp 
        rev += 1
    return rev

if __name__ == '__main__':
    assert jump([2, 3, 1, 1, 4]) == 2
