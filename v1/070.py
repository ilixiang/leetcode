#!/usr/bin/python3

def climbStairs(n):
    dp = [None] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    return climbStairsDp(n, dp)

def climbStairsDp(n, dp):
    if dp[n] != None:
        return dp[n]
    dp[n] = climbStairsDp(n - 1, dp) + climbStairsDp(n - 2, dp)
    return dp[n]

print(climbStairs(2))
print(climbStairs(3))
    

