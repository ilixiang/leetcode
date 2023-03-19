#!/usr/bin/python3

def maxProfit(prices):
    rev = l = r = 0
    for i in range(len(prices)):
        price = prices[i]
        if price < prices[l]:
            l = r = i
        if price > prices[r]:
            r = i
            rev = max(price - prices[l], rev)
    return rev

