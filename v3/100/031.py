#!/usr/bin/python3

def nextPermutation(nums):
    i = len(nums) - 1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1

    if i != 0:
        swap = len(nums) - 1
        while swap > 0 and nums[swap] <= nums[i - 1]:
            swap -= 1
        nums[i - 1], nums[swap] = nums[swap], nums[i - 1]
    
    left, right = i, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
