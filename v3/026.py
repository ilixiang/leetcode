#!/usr/bin/python3

def removeDuplicates(nums):
    end = cur = 0
    while cur < len(nums):
        if cur != 0 and nums[cur] == nums[cur - 1]:
            cur += 1
            continue
        nums[end] = nums[cur]
        end += 1
        cur += 1
    return end
