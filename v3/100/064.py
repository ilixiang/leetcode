#!/usr/bin/python3

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[None for j in range(n)] for i in range(m)]
    dp[m - 1][n - 1] = grid[m - 1][n - 1]

    def minPathSumDp(i, j):
        if dp[i][j] != None:
            return dp[i][j]
        
        rev = grid[i][j]
        if i == m - 1:
            rev += minPathSumDp(i, j + 1)
        elif j == n - 1:
            rev += minPathSumDp(i + 1, j)
        else:
            rev += min(minPathSumDp(i, j + 1), minPathSumDp(i + 1, j))
        dp[i][j] = rev
        return rev
    return minPathSumDp(0, 0)
