#!/usr/bin/python3

def searchRange(nums, target):
    low = high = -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) >> 1
        num = nums[mid]
        if num == target:
            low = mid
            right = mid
        elif num < target:
            left = mid + 1
        else:
            right = mid
    
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) >> 1
        num = nums[mid]
        if num == target:
            high = mid
            left = mid + 1
        elif num < target:
            left = mid + 1
        else:
            right = mid
    
    return [low, high]

