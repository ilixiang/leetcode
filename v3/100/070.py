#!/usr/bin/python3

def climbStairs(n):
    dp = [None for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1

    def climbStairsDp(i):
        if dp[i] != None:
            return dp[i]
        dp[i] = climbStairsDp(i - 1) + climbStairsDp(i - 2)
        return dp[i]
    return climbStairsDp(n)
