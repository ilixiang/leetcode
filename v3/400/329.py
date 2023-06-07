#!/usr/bin/python3

def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    cache = [[None for i in range(n)] for j in range(m)]
    def dp(i, j):
        if cache[i][j] != None:
            return cache[i][j]
        nextPathLength = 0
        if i > 0 and matrix[i - 1][j] < matrix[i][j]:
            nextPathLength = max(nextPathLength, dp(i - 1, j))
        if j > 0 and matrix[i][j - 1] < matrix[i][j]:
            nextPathLength = max(nextPathLength, dp(i, j - 1))
        if i < m - 1 and matrix[i + 1][j] < matrix[i][j]:
            nextPathLength = max(nextPathLength, dp(i + 1, j))
        if j < n - 1 and matrix[i][j + 1] < matrix[i][j]:
            nextPathLength = max(nextPathLength, dp(i, j + 1))
        cache[i][j] = 1 + nextPathLength
        return 1 + nextPathLength
    rev = 0
    for i in range(m):
        for j in range(n):
            rev = max(rev, dp(i, j))
    return rev
