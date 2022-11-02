#!/usr/bin/python3

def maxProfit(prices):
    minPrice = prices[0]
    maxPrice = minPrice
    maxProfit = 0
    for price in prices:
        if price < minPrice:
            minPrice = price
            maxPrice = price

        if price > maxPrice:
            maxPrice = price
        maxProfit = max(maxProfit, maxPrice - minPrice)
    return maxProfit 

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 5, 4, 3, 1]))

