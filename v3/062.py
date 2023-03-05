#!/usr/bin/python3

def uniquePaths(m, n):
    dp = [[None for j in range(n)] for i in range(m)]
    for i in range(m):
        dp[i][n - 1] = 1
    for j in range(n):
        dp[m - 1][j] = 1
    
    def uniquePathsDp(i, j):
        if dp[i][j] != None:
            return dp[i][j]
        
        dp[i][j] = uniquePathsDp(i + 1, j) + uniquePathsDp(i, j + 1)
        return dp[i][j]
    return uniquePathsDp(0, 0)
