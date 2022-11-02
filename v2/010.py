#!/usr/bin/python3

def isMatch(s, p):
    dp = [None] * (len(s) + 1)
    for i in range(0, len(dp)):
        dp[i] = [None] * (len(p) + 1)
        dp[i][len(p)] = False
    dp[len(s)][len(p)] = True
    return isMatchDp(s, p, 0, 0, dp)

def isMatchDp(s, p, i, j, dp):
    if dp[i][j] != None:
        return dp[i][j]
    
    if j + 1 < len(p) and p[j + 1] == '*':
        if i < len(s) and (s[i] == p[j] or p[j] == '.'):
            dp[i][j] = isMatchDp(s, p, i, j + 2, dp) \
                or isMatchDp(s, p, i + 1, j + 2, dp) \
                or isMatchDp(s, p, i + 1, j, dp)
        else:
            dp[i][j] = isMatchDp(s, p, i, j + 2, dp)
    else:
        if i < len(s) and (s[i] == p[j] or p[j] == '.'):
            dp[i][j] = isMatchDp(s, p, i + 1, j + 1, dp)
        else:
            dp[i][j] = False
    
    return dp[i][j]
