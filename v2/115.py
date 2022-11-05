#!/usr/bin/python3

def numDistinct(s, t):
    m = len(s)
    n = len(t)
    dp = [None] * m
    for i in range(0, len(dp)):
        dp[i] = [None] * n

    def numDistinctDp(i, j):
        if i == m and j != n:
            return 0
        
        if j == n:
            return 1
        
        if dp[i][j] != None:
            return dp[i][j]
        
        if m - i < n - j:
            dp[i][j] = 0
            return 0

        rev = 0
        if s[i] == t[j]:
            rev += numDistinctDp(i + 1, j + 1)
        rev += numDistinctDp(i + 1, j)
        dp[i][j] = rev
        return rev
    return numDistinctDp(0, 0)
