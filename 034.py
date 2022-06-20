#!/usr/bin/python3

def searchRange(nums, target):
    if len(nums) == 0:
        return [-1, -1]
    left, right = 0, len(nums)
    mid = (left + right) // 2
    while left < right:
        if target >= nums[mid]:
            left = mid + 1
        else:
            right = mid
        mid = (left + right) // 2
    if mid == 0 or nums[mid - 1] != target:
        return [-1, -1]
    top = mid - 1

    left, right = 0, len(nums)
    mid = (left + right) // 2
    while left < right:
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
        mid = (left + right) // 2
    bottom = mid
    return [bottom, top]

print(searchRange([9,9], 8)) 
print(searchRange([5,7,7,8,8,10], 6)) 
print(searchRange([5,7,7,8,8,10], 5)) 

