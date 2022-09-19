#!/usr/bin/python3

def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    dp = [None] * (len(s1) + 1)
    for i in range(0, len(s1) + 1):
        dp[i] = [None] * (len(s2) + 1)
    return isInterleaveDp(s1, 0, s2, 0, s3, 0, dp)

def isInterleaveDp(s1, i1, s2, i2, s3, i3, dp):
    if dp[i1][i2] != None:
        return dp[i1][i2]

    if i1 == len(s1):
        dp[i1][i2] = s2[i2:] == s3[i3:]
        return dp[i1][i2]

    if i2 == len(s2):
        dp[i1][i2] = s1[i1:] == s3[i3:]
        return dp[i1][i2]

    dp[i1][i2] = (s1[i1] == s3[i3] and isInterleaveDp(s1, i1 + 1, s2, i2, s3, i3 + 1, dp)) or (s2[i2] == s3[i3] and isInterleaveDp(s1, i1, s2, i2 + 1, s3, i3 + 1, dp))
    return dp[i1][i2]

print(isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
print(isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))

