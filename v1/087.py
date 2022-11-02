#!/usr/bin/python3

def isScramble(s1, s2):
    dp = {}
    for i in range(0, len(s1)):
        dp[i] = [None] * len(s1)
        dp[i][i] = set([s1[i]])
    s = isScrambleDp(s1, s2, dp)
    return dp[s1][s2]
    
def isScrambleDp(s1, s2, dp):
    if s1 in dp and s2 in dp[s1]:
        return dp[s1][s2]

    if s1 == s2:
        if not s1 in dp:
            dp[s1] = {}
        dp[s1][s2] = True
        return True

    length = len(s1)
    for i in range(0, length - 1):
        if (isScrambleDp(s1[0: i + 1], s2[0: i + 1], dp) and isScrambleDp(s1[i + 1: length], s2[i + 1: length], dp)) or (isScrambleDp(s1[0: i + 1], s2[length - i - 1: length], dp) and isScrambleDp(s1[i + 1: length], s2[0: length - i - 1], dp)):
            if not s1 in dp:
                dp[s1] = {}
            dp[s1][s2] = True
            return True
    if not s1 in dp:
        dp[s1] = {}
    dp[s1][s2] = False
    return False
        
print(isScramble('abcde', 'caebd'))
print(isScramble('a', 'a'))

