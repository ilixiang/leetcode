#!/usr/bin/python3

def wordBreak(s, wordDict):
    m = len(s)
    wordSet = set(wordDict)
    strides = set(len(word) for word in wordDict)
    dp = [None] * (m + 1)
    dp[m] = [[]]

    def recursive(i):
        if dp[i]:
            return dp[i]
        
        rev = []
        for stride in strides:
            if i + stride <= m and s[i:i + stride] in wordSet:
                suffixes = recursive(i + stride)
                for suffix in suffixes:
                    rev.append([s[i:i + stride]] + suffix)
        dp[i] = rev
        return rev
    return list(map(lambda x: ' '.join(x), recursive(0)))
