#!/usr/bin/python3

def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid[m - 1][n - 1] == 1:
        return 0

    dp = [None] * m
    for i in range(0, m):
        dp[i] = [None] * n
    dp[m - 1][n - 1] = 1

    return uniquePathsWithObstaclesDp(obstacleGrid, m, n, 0, 0, dp)

def uniquePathsWithObstaclesDp(obstacleGrid, m, n, x, y, dp):
    if dp[x][y] != None:
        return dp[x][y]

    if obstacleGrid[x][y] == 1:
        dp[x][y] = 0
        return 0
    
    res = 0
    if x != m - 1:
        res += uniquePathsWithObstaclesDp(obstacleGrid, m, n, x + 1, y, dp)
    if y != n - 1:
        res += uniquePathsWithObstaclesDp(obstacleGrid, m, n, x, y + 1, dp)
    dp[x][y] = res
    return res
