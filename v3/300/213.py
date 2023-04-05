#!/usr/bin/python3

def rob(nums):
    if len(nums) == 0:
        return 0

    cache = [None] * len(nums)
    def dp(right, start):
        if start >= right:
            return 0
        
        if cache[start] != None:
            return cache[start]
        
        cache[start] = max(nums[start] + dp(right, start + 2), dp(right, start + 1))
        return cache[start]
    
    robFirstMaxValue = nums[0] + dp(len(nums) - 1, 2)

    for i in range(len(nums)):
        cache[i] = None
    notRobFirstMaxValue = dp(len(nums), 1)
    return max(robFirstMaxValue, notRobFirstMaxValue)
