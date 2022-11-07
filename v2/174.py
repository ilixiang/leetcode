#!/usr/bin/python3

def calculateMinimumHP(dungeon):
    m = len(dungeon)
    n = len(dungeon[0])
    dp = [None] * m
    for i in range(0, m):
        dp[i] = [None] * n
    
    def calculateDp(i, j):
        if dp[i][j] != None:
            return dp[i][j]

        if i == m - 1 and j == n - 1:
            dp[i][j] = 1 if dungeon[i][j] >= 0 else (1 - dungeon[i][j])
        elif i == m - 1:
            dp[i][j] = max(1, calculateDp(i, j + 1) - dungeon[i][j])
        elif j == n - 1:
            dp[i][j] = max(1, calculateDp(i + 1, j) - dungeon[i][j])
        else:
            right = calculateDp(i, j + 1)
            down = calculateDp(i + 1, j)
            dp[i][j] = max(1, min(right, down) - dungeon[i][j])
        return dp[i][j]
    
    return calculateDp(0, 0)
