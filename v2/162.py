#!/usr/bin/python3

def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[left] < nums[right]:
            left = mid + 1
        elif nums[left] > nums[right]:
            right = mid - 1
        else:
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid - 1
    return (left + right) >> 1
