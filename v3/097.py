#!/usr/bin/python3

def isInterleave(s1, s2, s3):
    m, n, l = len(s1), len(s2), len(s3)
    if m + n != l:
        return False
    
    dp = [[None for j in range(n + 1)] for i in range(m + 1)]
    dp[m][n] = True
    def isInterleaveDp(i, j):
        if dp[i][j] != None:
            return dp[i][j]
        dp[i][j] = (i < m and s1[i] == s3[i + j] and isInterleaveDp(i + 1, j))\
            or (j < n and s2[j] == s3[i + j] and isInterleaveDp(i, j + 1))
        return dp[i][j]
    return isInterleaveDp(0, 0)
