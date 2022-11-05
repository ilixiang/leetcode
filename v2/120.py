#!/usr/bin/python3

def minimumTotal(triangle):
    m = len(triangle)
    dp = [None] * m
    for i in range(0, len(dp)):
        dp[i] = [None] * (i + 1)
    def minimulTotalDp(i, j):
        if dp[i][j] != None:
            return dp[i][j]

        if i == m - 1:
            dp[i][j] = triangle[i][j]
            return dp[i][j]

        dp[i][j] = triangle[i][j] + min(minimulTotalDp(i + 1, j), minimulTotalDp(i + 1, j + 1))
        return dp[i][j]
    return minimulTotalDp(0, 0)

