#!/usr/bin/python3

def maxProfit(prices):
    cache = [None] * len(prices)
    def dp(idx):
        if idx >= len(prices):
            return (0, 0)
        if cache[idx] != None:
            return cache[idx]
        
        sell = max(prices[idx] + dp(idx + 2)[0], dp(idx + 1)[1])
        buy = max(-prices[idx] + sell, dp(idx + 1)[0])
        rev = cache[idx] = (buy, sell)
        return rev
    return dp(0)[0]
