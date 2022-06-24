#!/usr/bin/python3

def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid[m - 1][n - 1] == 1:
        return 0

    dp = [None] * m
    for i in range(0, m):
        arr = [None] * n
        for j in range(0, n):
            if obstacleGrid[i][j] == 1:
                arr[j] = 0
        dp[i] = arr
    dp[m - 1][n - 1] = 1
    return uniquePathsWithObstaclesDp(m, n, 0, 0, dp)

def uniquePathsWithObstaclesDp(m, n, mIndex, nIndex, dp):
    if mIndex >= m or nIndex >= n:
        return 0
    if dp[mIndex][nIndex] != None:
        return dp[mIndex][nIndex]

    dp[mIndex][nIndex] = uniquePathsWithObstaclesDp(m, n, mIndex + 1, nIndex, dp) + uniquePathsWithObstaclesDp(m, n, mIndex, nIndex + 1, dp)
    return dp[mIndex][nIndex]

print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(uniquePathsWithObstacles([[0,1],[0,0]]))
print(uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))

