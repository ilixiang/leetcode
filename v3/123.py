#!/usr/bin/python3

def maxProfit(prices):
    BUY, SELL = 0, 1
    mem = [[None for j in range(len(prices))] for i in range(2)]
    def dp(i, n):
        if n >= 2 or i >= len(prices):
            return (0, 0)

        if mem[n][i] != None:
            return mem[n][i]

        sellMaxProfit = max(prices[i] + dp(i + 1, n + 1)[BUY], dp(i + 1, n)[SELL])
        buyMaxProfit = max(-1 * prices[i] + sellMaxProfit, dp(i + 1, n)[BUY])
        mem[n][i] = (buyMaxProfit, sellMaxProfit)
        return mem[n][i]
    return dp(0, 0)[BUY]
