#!/usr/bin/python3

def numDecodings(s):
    n = len(s)
    dp = [None] * n
    return numDecodingsDp(s, n, 0, dp)

def numDecodingsDp(s, n, i, dp):
    if i == n:
        return 1
    
    if dp[i] != None:
        return dp[i]

    if s[i] == '0':
        dp[i] = 0
        return 0

    rev = numDecodingsDp(s, n, i + 1, dp)
    if i + 1 < n and int(s[i: i + 2]) <= 26:
        rev += numDecodingsDp(s, n, i + 2, dp)
    dp[i] = rev
    return rev
