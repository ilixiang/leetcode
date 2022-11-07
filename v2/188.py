#!/usr/bin/python3

def maxProfit(k, prices):
    m = len(prices)
    maxTxCount = 2 * k
    dp = [None] * m
    for i in range(0, m):
        dp[i] = [None] * maxTxCount
    
    def maxProfitDp(txCount, pIndex):
        if txCount == maxTxCount or pIndex == m:
            return 0

        if dp[pIndex][txCount] != None:
            return dp[pIndex][txCount]
        
        current = (-1 if (txCount & 1) == 0 else 1) * prices[pIndex]
        dp[pIndex][txCount] = max(current + maxProfitDp(txCount + 1, pIndex), maxProfitDp(txCount, pIndex + 1))
        return dp[pIndex][txCount]
    
    return maxProfitDp(0, 0)

