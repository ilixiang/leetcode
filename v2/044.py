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
    
    if p[j] == '*':
        dp[i][j] = isMatchDp(s, p, i, j + 1, dp) or (i < len(s) and isMatchDp(s, p, i + 1, j, dp))
    elif p[j] == '?':
        dp[i][j] = i < len(s) and isMatchDp(s, p, i + 1, j + 1, dp)
    else:
        dp[i][j] = i < len(s) and j < len(p) and s[i] == p[j] and isMatchDp(s, p, i + 1, j + 1, dp)
    return dp[i][j]

if __name__ == '__main__':
    print(isMatch("", "******"))
