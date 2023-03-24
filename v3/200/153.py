#!/usr/bin/python3

def findMin(nums):
    left, right = 0, len(nums) - 1
    rev = nums[0]
    while left <= right:
        mid = (left + right) >> 1
        if nums[left] > nums[right]:
            if nums[mid] <= nums[right]:
                rev = min(rev, nums[mid])
                right = mid - 1
            else:
                rev = min(rev, nums[right])
                left = mid + 1
                right -= 1
        else:
            return min(rev, nums[left])
    return rev
