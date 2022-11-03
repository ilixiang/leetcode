#!/usr/bin/python3

def firstMissingPositive(nums):
    minPositive = 1
    for num in nums:
        if num > 0:
            minPositive = min(minPositive, num)
    
    if minPositive != 1:
        return 1
    
    for i in range(0, len(nums)):
        if nums[i] >= 0:
            nums[i] -= minPositive
    
    for i in range(0, len(nums)):
        num = nums[i]
        while num >= 0 and num < len(nums) and nums[num] != num:
            tmp = nums[num]
            nums[num] = num
            num = tmp
        if num < 0 or num >= len(nums):
            nums[i] = num
    
    for i in range(0, len(nums)):
        if nums[i] != i:
            return i + minPositive
    return len(nums)
