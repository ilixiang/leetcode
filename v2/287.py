#!/usr/bin/python3

def findDuplicate(nums):
    fast = nums[nums[0]]
    slow = nums[0]
    while fast != slow:
        fast = nums[nums[fast]]
        slow = nums[slow]
    
    fast = 0
    while fast != slow:
        fast = nums[fast]
        slow = nums[slow]
    return fast
