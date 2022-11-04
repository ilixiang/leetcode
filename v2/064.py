#!/usr/bin/python3

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])

    dp = [None] * m
    for i in range(0, m):
        dp[i] = [None] * n

    return minPathSumDp(grid, m, n, 0, 0, dp)

def minPathSumDp(grid, m, n, x, y, dp):
    if dp[x][y] != None:
        return dp[x][y]
    
    res = grid[x][y]
    downMinSum = None
    if x != m - 1:
        downMinSum = minPathSumDp(grid, m, n, x + 1, y, dp)
    rightMinSum = None
    if y != n - 1:
        rightMinSum = minPathSumDp(grid, m, n, x, y + 1, dp)
    if downMinSum == None and rightMinSum == None:
        dp[x][y] = res
        return res
    
    if downMinSum == None:
        res += rightMinSum
    elif rightMinSum == None:
        res += downMinSum
    else:
        res += min(rightMinSum, downMinSum)
    dp[x][y] = res
    return res
