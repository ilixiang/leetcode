#!/usr/bin/python3

def isMatch(s, p):
    dp = [[None for j in range(len(p) + 1)] for i in range(len(s) + 1)]
    for i in range(len(s)):
        dp[i][len(p)] = False
    dp[len(s)][len(p)] = True

    def isMatchDp(i, j):
        if dp[i][j] != None:
            return dp[i][j]
        
        if p[j] == '*':
            dp[i][j] = (i < len(s) and isMatchDp(i + 1, j)) or isMatchDp(i, j + 1)
        else:
            dp[i][j] = i < len(s) and (p[j] == '?' or s[i] == p[j]) and isMatchDp(i + 1, j + 1)
        return dp[i][j]
    return isMatchDp(0, 0)

if __name__ == '__main__':
    assert isMatch('a', 'aa') == False
    assert isMatch('aa', '*') == True
    assert isMatch('cb', '?a') == False
