#!/usr/bin/python3

def maxProfit(k, prices):
    dp = [None] * (2 * k)
    for i in range(0, 2 * k):
        dp[i] = [None] * len(prices)
    return maxProfitDp(k, prices, 0, 0, dp)

def maxProfitDp(k, prices, index, operation, dp):
    if operation == 2 * k or index == len(prices):
        return 0

    if dp[operation][index] == None:
        doNothingProfit = maxProfitDp(k, prices, index + 1, operation, dp)
        doOperationProfit = (-1 if operation & 1 == 0 else 1) * prices[index] + maxProfitDp(k, prices, index + 1, operation + 1, dp)
        dp[operation][index] = max(doNothingProfit, doOperationProfit)
    return dp[operation][index]
            
print(maxProfit(2, [2, 4, 1]))
print(maxProfit(2, [3, 2, 6, 5, 0, 3]))

