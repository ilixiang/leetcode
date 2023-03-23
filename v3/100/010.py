#!/usr/bin/python3

def isMatch(s, p):
    dp = [[None for j in range(len(p) + 1)] for i in range(len(s) + 1)]
    for i in range(len(s) + 1):
        dp[i][len(p)] = False
    dp[len(s)][len(p)] = True

    def isMatchDp(i, j):
        if dp[i][j] != None:
            return dp[i][j]

        if j + 1 < len(p) and p[j + 1] == '*':
            dp[i][j] = (i < len(s) and (p[j] == '.' or s[i] == p[j]) and isMatchDp(i + 1, j)) or isMatchDp(i, j + 2)
        else:
            dp[i][j] = i < len(s) and (p[j] == '.' or s[i] == p[j]) and isMatchDp(i + 1, j + 1)
        return dp[i][j]
    return isMatchDp(0, 0)

if __name__ == '__main__':
    assert isMatch('aa', 'a') == False 
    assert isMatch('aa', 'a*') == True
    assert isMatch('aaaaaaaaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*') == False
