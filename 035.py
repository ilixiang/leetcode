#!/usr/bin/python3

def searchInsert(nums, target):
    left = 0
    right = len(nums)
    mid = (left + right) // 2
    while left < right:
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
        mid = (left + right) // 2
    return mid

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))

