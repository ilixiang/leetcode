#!/usr/bin/python3

def rob(nums):
    dp = [None] * len(nums)
    return robDp(nums, 0, dp)

def robDp(nums, startIndex, dp):
    if startIndex >= len(nums):
        return 0

    if dp[startIndex] != None:
        return dp[startIndex]

    dp[startIndex] = max(nums[startIndex] + robDp(nums, startIndex + 2, dp), robDp(nums, startIndex + 1, dp))
    return dp[startIndex]

print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))

