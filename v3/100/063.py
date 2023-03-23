#!/usr/bin/python3

def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
        return 0

    dp = [[None for j in range(n)] for i in range(m)]
    dp[m - 1][n - 1] = 1
    
    def uniquePathsWithObstaclesDp(i, j):
        if dp[i][j] != None:
            return dp[i][j]
        
        if obstacleGrid[i][j] == 1:
            dp[i][j] = 0
        else:
            tmp = 0
            if i < m - 1:
                tmp += uniquePathsWithObstaclesDp(i + 1, j)
            if j < n - 1:
                tmp += uniquePathsWithObstaclesDp(i, j + 1)
            dp[i][j] = tmp
        return dp[i][j]
    return uniquePathsWithObstaclesDp(0, 0)

