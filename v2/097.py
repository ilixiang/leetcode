#!/usr/bin/python3

def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    dp = [None] * (len(s1) + 1)
    for i in range(0, len(dp)):
        dp[i] = [None] * (len(s2) + 1)
    return isInterleaveDp(s1, s2, s3, 0, 0, dp)

def isInterleaveDp(s1, s2, s, i1, i2, dp):
    if dp[i1][i2] != None:
        return dp[i1][i2]

    rev = False
    if i1 == len(s1):
        rev = s[i1 + i2:] == s2[i2:]
    elif i2 == len(s2):
        rev = s[i1 + i2:] == s1[i1:]
    else:
        rev = i1 < len(s1) and s1[i1] == s[i1 + i2] and isInterleaveDp(s1, s2, s, i1 + 1, i2, dp)
        if not rev:
            rev = i2 < len(s2) and s2[i2] == s[i1 + i2] and isInterleaveDp(s1, s2, s, i1, i2 + 1, dp)
    
    dp[i1][i2] = rev
    return rev

