#!/usr/bin/python3

def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[None for j in range(n + 1)] for i in range(m + 1)]
    dp[m][n] = 0
    for i in range(m):
        dp[i][n] = m - i
    for j in range(n):
        dp[m][j] = n - j

    def minDistanceDp(i, j):
        if dp[i][j] != None:
            return dp[i][j]
        
        if word1[i] == word2[j]:
            dp[i][j] = minDistanceDp(i + 1, j + 1)
        else:
            dp[i][j] = 1 + min(minDistanceDp(i + 1, j), minDistanceDp(i, j + 1), minDistanceDp(i + 1, j + 1))
        return dp[i][j]
    return minDistanceDp(0, 0)