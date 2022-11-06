#!/usr/bin/python3

def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return (left + right) >> 1

