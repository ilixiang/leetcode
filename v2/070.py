#!/usr/bin/python3

def climbStairs(n):
    dp = [None] * (n + 1)
    return climbStairsDp(n, 0, dp)

def climbStairsDp(n, cur, dp):
    if dp[cur] != None:
        return dp[cur]

    if cur == n:
        dp[cur] = 1
        return 1
    
    res = 0
    res += climbStairsDp(n, cur + 1, dp)
    if cur + 2 <= n:
        res += climbStairsDp(n, cur + 2, dp)
    dp[cur] = res
    return res
    