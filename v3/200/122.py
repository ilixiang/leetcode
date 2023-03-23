#!/usr/bin/python3

def maxProfit(prices):
    rev, i, m = 0, 1, len(prices)
    while i < m:
        if prices[i] >= prices[i - 1]:
            rev += prices[i] - prices[i - 1]
        i += 1
    return rev
