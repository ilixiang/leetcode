#!/usr/bin/python3

def removeDumplicates(nums):
    if len(nums) < 2:
        return len(nums)
    left, right = -1, 0
    while right < len(nums):
        if right > 0:
            while right < len(nums) and nums[right] == nums[right - 1]:
                right = right + 1
        if right < len(nums):
            nums[left + 1] = nums[right]
            left = left + 1
            right = right + 1
    return left + 1

print(removeDumplicates([1,1,2]))

