#!/usr/bin/python3

def searchInsert(nums, target):
    left, right = 0, len(nums)
    rev = len(nums)
    while left < right:
        mid = (left + right) >> 1
        num = nums[mid]
        if num == target:
            return mid
        elif num < target:
            left = mid + 1
        else:
            rev = mid
            right = mid
    return rev


