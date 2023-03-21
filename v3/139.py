#!/usr/bin/python3

def wordBreak(s, wordDict):
    m = len(s)
    wordSet = set(wordDict)
    strides = set(len(word) for word in wordDict)
    dp = [None] * (m + 1)
    dp[m] = True
    
    def recursive(i):
        if dp[i] != None:
            return dp[i]
        for stride in strides:
            if i + stride <= m and s[i:i + stride] in wordSet and recursive(i + stride):
                dp[i] = True
                return True
        dp[i] = False
        return False
    return recursive(0)
