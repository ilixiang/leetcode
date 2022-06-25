#!/usr/bin/python3

def sortColors(nums):
    left = -1
    right = len(nums)
    mid = 0
    while mid < right:
        if nums[mid] == 0:
            tmp = nums[mid]
            nums[mid] = nums[left + 1]
            nums[left + 1] = tmp
            left = left + 1
            mid = mid + 1
        elif nums[mid] == 2:
            tmp = nums[mid]
            nums[mid] = nums[right - 1]
            nums[right - 1] = tmp
            right = right - 1
        else:
            mid = mid + 1

nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)

