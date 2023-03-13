#!/usr/bin/python3

def numTrees(n):
    dp = [-1] * (n + 1)
    dp[0] = 1

    def numTreesDp(n):
        if dp[n] != -1:
            return dp[n]
        
        rev = 0
        for i in range(n):
            leftNum = numTreesDp(i)
            rightNum = numTreesDp(n - 1 - i)
            rev += leftNum * rightNum
        dp[n] = rev
        return rev
    return numTreesDp(n)
