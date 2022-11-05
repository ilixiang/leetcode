#!/usr/bin/python3

def maxProfit(prices):
    minPrice = prices[0]
    profit = 0
    for price in prices:
        if price > minPrice:
            profit = max(profit, price - minPrice)
        else:
            minPrice = price
    return profit
