#!/usr/bin/python3

def maxProfit(k, prices):
    BUY, SELL = 0, 1
    m = len(prices)
    cache = [[None for j in range(m)] for i in range(k)]

    def dp(n, i):
        if n >= k or i >= m:
            return (0, 0)
        
        if cache[n][i] != None:
            return cache[n][i]
        
        sellMaxProfit = max(prices[i] + dp(n + 1, i + 1)[BUY], dp(n, i + 1)[SELL])
        buyMaxProfit = max(sellMaxProfit - prices[i], dp(n, i + 1)[BUY])
        cache[n][i] = (buyMaxProfit, sellMaxProfit)
        return cache[n][i]
    return dp(0, 0)[BUY]
