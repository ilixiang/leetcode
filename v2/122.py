#!/usr/bin/python3

def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    i = 1
    profit = 0
    minPrice = prices[0]
    while i < len(prices):
        if prices[i] >= prices[i - 1]:
            i += 1
            continue
        profit += prices[i - 1] - minPrice
        minPrice = prices[i]
        i += 1
    profit += prices[len(prices) - 1] - minPrice
    return profit
