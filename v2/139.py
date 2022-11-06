#!/usr/bin/python3

def wordBreak(s, words):
    m = len(s)
    dp = [None] * m
    lookup = set(words)

    def wordBreakDp(i):
        if i == m:
            return True
        
        if dp[i] != None:
            return dp[i]
        
        j = i + 1
        while j <= m:
            if s[i:j] in lookup and wordBreakDp(j):
                dp[i] = True
                return True
            j += 1
        dp[i] = False
        return False

    return wordBreakDp(0)
