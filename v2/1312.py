#!/usr/bin/python3

def minInsertions(s):
    dp = [[None for j in range(0, len(s))] for i in range(0, len(s))]
    def recursive(left, right):
        if left >= right:
            return 0
        
        if dp[left][right]:
            return dp[left][right]
        
        if s[left] == s[right]:
            dp[left][right] = recursive(left + 1, right - 1)
        else:
            dp[left][right] = 1 + min(recursive(left, right - 1), recursive(left + 1, right))
        return dp[left][right]
    return recursive(0, len(s) - 1)