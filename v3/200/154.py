#!/usr/bin/python3

def findMin(nums):
    if len(nums) == 0:
        return None

    left, right = 0, len(nums) - 1
    rev = nums[0]
    while left <= right:
        mid = (left + right) >> 1
        if nums[left] < nums[right]:
            rev = min(rev, nums[left])
            return rev
        elif nums[left] > nums[right]:
            if nums[mid] <= nums[right]:
                rev = min(rev, nums[mid])
                right = mid - 1
            else:
                rev = min(rev, nums[right])
                left = mid
                right -= 1
        else:
            rev = min(rev, nums[right])
            right -= 1
            while left <= right and nums[right] == nums[right + 1]:
                right -= 1
    return rev
