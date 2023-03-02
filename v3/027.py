#!/usr/bin/python3

def removeElement(nums, val):
    end = cur = 0
    while cur < len(nums):
        if nums[cur] == val:
            cur += 1
            continue
        
        nums[end] = nums[cur]
        end += 1
        cur += 1
    return end
