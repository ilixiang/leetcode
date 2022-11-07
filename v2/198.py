#!/usr/bin/python3

def rob(nums):
    m = len(nums)
    dp = [None] * m

    def robDp(i):
        if i >= m:
            return 0

        if dp[i] != None:
            return dp[i]
        
        dp[i] = max(nums[i] + robDp(i + 2), robDp(i + 1))
        return dp[i]
    return robDp(0)
