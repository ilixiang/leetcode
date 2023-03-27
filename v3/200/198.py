#!/usr/bin/python3

def rob(nums):
    m = len(nums)
    cache = [None for i in range(m)]

    def dp(start):
        if start >= m:
            return 0
        if cache[start] != None:
            return cache[start]
        
        cache[start] = max(nums[start] + dp(start + 2), dp(start + 1))
        return cache[start]
    return dp(0)

