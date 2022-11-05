#!/usr/bin/python3

def maxProfit(prices):
    m = len(prices)
    dp = [None] * m
    for i in range(0, len(dp)):
        dp[i] = [None] * 4
    
    def maxProfitDp(start, count, dp):
        if start == m or count == 4:
            return 0

        if dp[start][count] != None:
            return dp[start][count]
        
        rev = 0
        if count & 1 == 1:
            rev = max(prices[start] + maxProfitDp(start, count + 1, dp), maxProfitDp(start + 1, count, dp))
        else:
            rev = max(maxProfitDp(start, count + 1, dp) - prices[start], maxProfitDp(start + 1, count, dp))
        dp[start][count] = rev
        return rev
    
    return maxProfitDp(0, 0, dp)
