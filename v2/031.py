#!/usr/bin/python3

def nextPermutation(nums):
    i = len(nums) - 1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1

    right = len(nums) - 1
    left = i
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    if i != 0:
        swapIndex = i - 1
        while nums[i] <= nums[swapIndex]:
            i += 1
        nums[swapIndex], nums[i] = nums[i], nums[swapIndex]

    