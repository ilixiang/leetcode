#!/usr/bin/python3

def uniquePaths(m, n):
    dp = [None] * m
    for i in range(0, m):
        dp[i] = [None] * n
    dp[m - 1][n - 1] = 1
    
    return uniquePathsDp(m, n, 0, 0, dp)

def uniquePathsDp(m, n, x, y, dp):
    if dp[x][y] != None:
        return dp[x][y]

    res = 0
    if x != m - 1:
        res += uniquePathsDp(m, n, x + 1, y, dp)
    if y != n - 1:
        res += uniquePathsDp(m, n, x, y + 1, dp)
    dp[x][y] = res
    return res
