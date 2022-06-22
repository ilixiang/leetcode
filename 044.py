#!/usr/bin/python3

def isMatch(s, p):
    dp = []
    for pIndex in range(0, len(p)):
        dp.append([None] * (len(s) + 1))
    dp.append([False] * (len(s) + 1))
    dp[len(p)][len(s)] = True
    return match(s, p, 0, 0, dp)

def match(s, p, sIndex, pIndex, dp):
    if dp[pIndex][sIndex] != None:
        return dp[pIndex][sIndex]

    pChar = p[pIndex]
    if pChar == '*':
        dp[pIndex][sIndex] = match(s, p, sIndex, pIndex + 1, dp) or (sIndex < len(s) and match(s, p, sIndex + 1, pIndex, dp))
    elif pChar == '?':
        dp[pIndex][sIndex] = sIndex < len(s) and match(s, p, sIndex + 1, pIndex + 1, dp)
    else:
        dp[pIndex][sIndex] = sIndex < len(s) and s[sIndex] == pChar and match(s, p, sIndex + 1, pIndex + 1, dp)
    return dp[pIndex][sIndex]

print(isMatch('aa', 'a'))
print(isMatch('aa', '*'))
print(isMatch('ba', '?a'))

