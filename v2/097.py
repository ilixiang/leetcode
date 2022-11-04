#!/usr/bin/python3

def isInterleave(s1, s2, s3):
    dp = {}
    return isInterleaveDp(s3, s1, s2, 0, 0, 0, dp, 'a', 'b') or isInterleave(s3, s2, s1, 0, 0, 0, dp, 'b', 'a')

def isInterleaveDp(target, cur, next, tIndex, cIndex, nIndex, dp, cPrefix, nPrefix):
    if tIndex == len(target):
        return True
    
    key = '%s%ds%d'%(cPrefix, cIndex, tIndex)
    if key in dp:
        return dp[key]

    rev = False
    while cIndex < len(cur) and tIndex < len(target) and cur[cIndex] == target[tIndex]:
        if isInterleaveDp(target, next, cur, tIndex + 1, nIndex, cIndex + 1, dp, nPrefix, cPrefix):
            rev = True
            break
        cIndex += 1
        tIndex += 1
    if cIndex == len(cur):
        rev = True
    rev = False
    dp[key] = rev
    return rev
