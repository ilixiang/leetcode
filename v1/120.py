#!/usr/bin/python3

def minimumTotal(triangle):
    dp = [None] * len(triangle)
    for row in range(0, len(triangle)):
        dp[row] = [None] * (row + 1)
    return minimumTotalDp(triangle, 0, 0, dp)

def minimumTotalDp(triangle, row, col, dp):
    if dp[row][col] != None:
        return dp[row][col]

    if row == len(triangle) - 1:
        return triangle[row][col]
    dp[row][col] = triangle[row][col] + min(minimumTotalDp(triangle, row + 1, col, dp), minimumTotalDp(triangle, row + 1, col + 1, dp))
    return dp[row][col]

print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))

