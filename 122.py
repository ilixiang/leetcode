#!/usr/bin/python3

def maxProfit(prices):
    profit = 0
    index = 0
    while index < len(prices):
        while index + 1 < len(prices) and prices[index + 1] < prices[index]:
            index = index + 1
        price = prices[index]
        print('START INDEX', index)
        while index + 1 < len(prices) and prices[index + 1] >= prices[index]:
            index = index + 1
        print('END INDEX', index)
        profit = profit + prices[index] - price
        index = index + 1
    return profit

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 4, 5]))
print(maxProfit([7, 6, 4, 3, 1]))

