#!/usr/bin/python3

def searchRange(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    mid = (left + right) // 2
    if mid == len(nums) or nums[mid] != target:
        return [-1, -1]
    first = mid

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid
        else:
            left = mid + 1
    mid = (left + right) // 2
    second = mid - 1
    return [first, second]
