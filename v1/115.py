#!/usr/bin/python3

def numDistinct(s, t):
    dp = [None] * (len(s) + 1)
    for sIndex in range(0, len(s) + 1):
        dp[sIndex] = [None] * (len(t) + 1)
        for tIndex in range(0, len(t) + 1):
            if tIndex == len(t):
                dp[sIndex][tIndex] = 1
                continue
            if len(s) - sIndex < len(t) - tIndex:
                dp[sIndex][tIndex] = 0

    numDistinctDp(s, t, 0, 0, dp)
    return dp[0][0]

def numDistinctDp(s, t, sIndex, tIndex, dp):
    if dp[sIndex][tIndex] != None:
        return dp[sIndex][tIndex]
    result = 0
    if s[sIndex] == t[tIndex]:
        result = numDistinctDp(s, t, sIndex + 1, tIndex, dp) + numDistinctDp(s, t, sIndex + 1, tIndex + 1, dp)
    else:
        result = numDistinctDp(s, t, sIndex + 1, tIndex, dp)
    dp[sIndex][tIndex] = result
    return result

print(numDistinct('b', 'a'))
print(numDistinct('eee', 'eee'))
print(numDistinct('rabbbit', 'rabbit'))
print(numDistinct('babgbag', 'bag'))

