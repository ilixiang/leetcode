#!/usr/bin/python3

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        print(left, right)
        mid = (left + right) // 2
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[right] < nums[mid]:
            left = mid + 1
        elif nums[mid] < nums[left]:
            right = mid
        else:
            return nums[left]
    return nums[left]

print(findMin([1]))
