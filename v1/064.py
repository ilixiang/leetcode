#!/usr/bin/python3

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [None] * m
    for i in range(0, m):
        arr = [None] * n
        dp[i] = arr
    dp[m - 1][n - 1] = grid[m - 1][n - 1]
    for i in range(1, m):
        dp[m - 1 - i][n - 1] = dp[m - i][n - 1] + grid[m - 1 - i][n - 1]
    for j in range(1, n):
        dp[m - 1][n - 1 - j] = dp[m - 1][n - j] + grid[m - 1][n - 1 - j]
    return minPathSumDp(grid, 0, 0, dp)

def minPathSumDp(grid, mIndex, nIndex, dp):
    if dp[mIndex][nIndex] != None:
        return dp[mIndex][nIndex]

    dp[mIndex][nIndex] = grid[mIndex][nIndex] + min(minPathSumDp(grid, mIndex + 1, nIndex, dp), minPathSumDp(grid, mIndex, nIndex + 1, dp))
    return dp[mIndex][nIndex]

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))


