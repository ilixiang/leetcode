#!/usr/bin/python3

def isScramble(s1, s2):
    dp = {}
    return isScrambleRecursive(s1, s2, 0, len(s1), 0, len(s2), dp)

def isScrambleRecursive(s1, s2, l1, r1, l2, r2, dp):
    key = 'l%dr%dl%dr%d'%(l1, r1, l2, r2)
    if key in dp:
        return dp[key]

    if s1[l1: r1] == s2[l2: r2]:
        dp[key] = True
        return True

    m = {}
    for i in range(l1, r1):
        if not s1[i] in m:
            m[s1[i]] = 1
        else:
            m[s1[i]] += 1
    count = len(m)
    for i in range(l2, r2):
        if not s2[i] in m:
            return False
        else:
            m[s2[i]] -= 1
            if m[s2[i]] == 0:
                count -= 1
    if count != 0:
        return False
    
    for i in range(1, r1 - l1):
        if (isScrambleRecursive(s1, s2, l1, l1 + i, l2, l2 + i, dp) and isScrambleRecursive(s1, s2, l1 + i, r1, l2 + i, r2, dp))\
            or (isScrambleRecursive(s1, s2, l1, l1 + i, r2 - i, r2, dp) and isScrambleRecursive(s1, s2, l1 + i, r1, l2, r2 - i, dp)):
            dp[key] = True
            return True
    dp[key] = False
    return False
