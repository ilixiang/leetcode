#!/usr/bin/python3

def minDistance(word1, word2):
    dp = [None] * len(word1)
    for i in range(0, len(word1)):
        dp[i] = [None] * len(word2)
    return minDistanceDp(word1, word2, 0, 0, dp)

def minDistanceDp(word1, word2, i1, i2, dp):
    if i1 == len(word1):
        return len(word2) - i2
    if i2 == len(word2):
        return len(word1) - i1

    if dp[i1][i2] != None:
        return dp[i1][i2]

    if word1[i1] == word2[i2]:
        dp[i1][i2] = minDistanceDp(word1, word2, i1 + 1, i2 + 1, dp)
    else:
        dp[i1][i2] = min(minDistanceDp(word1, word2, i1, i2 + 1, dp), minDistanceDp(word1, word2, i1 + 1, i2, dp), minDistanceDp(word1, word2, i1 + 1, i2 + 1, dp)) + 1
    return dp[i1][i2]

print(minDistance('horse', 'ros'))
print(minDistance('intention', 'execution'))

