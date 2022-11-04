#!/usr/bin/python3

def minDistance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    dp = [None] * (len1 + 1)
    for i in range(0, len(dp)):
        dp[i] = [None] * (len2 + 1)
    
    return minDistanceDp(word1, word2, len1, len2, 0, 0, dp)

def minDistanceDp(word1, word2, len1, len2, i1, i2, dp):
    if dp[i1][i2] != None:
        return dp[i1][i2]
    
    if i1 == len1:
        dp[i1][i2] = len2 - i2
        return dp[i1][i2]
    
    if i2 == len2:
        dp[i1][i2] = len1 - i1
        return dp[i1][i2]
    
    if word1[i1] == word2[i2]:
        dp[i1][i2] = minDistanceDp(word1, word2, len1, len2, i1 + 1, i2 + 1, dp)
    else:
        deleteDistance = minDistanceDp(word1, word2, len1, len2, i1 + 1, i2, dp)
        insertDistance = minDistanceDp(word1, word2, len1, len2, i1, i2 + 1, dp)
        replaceDistance = minDistanceDp(word1, word2, len1, len2, i1 + 1, i2 + 1, dp)
        dp[i1][i2] = 1 + min(deleteDistance, insertDistance, replaceDistance)
    return dp[i1][i2]
