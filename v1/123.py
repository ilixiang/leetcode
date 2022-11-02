#!/usr/bin/python3

def maxProfit(prices):
    leftMaxProfits = [0] * len(prices)
    rightMaxProfits = [0] * len(prices)

    leftMin = prices[0]
    for i in range(1, len(prices)):
        leftMin = min(leftMin, prices[i])
        leftMaxProfits[i] = max(leftMaxProfits[i - 1], prices[i] - leftMin)
        
    rightMax = prices[len(prices) - 1]
    for i in range(len(prices) - 2, -1, -1):
        rightMax = max(rightMax, prices[i])
        rightMaxProfits[i] = max(rightMaxProfits[i + 1], rightMax - prices[i])

    rev = 0
    for i in range(0, len(prices)):
        rev = max(rev, leftMaxProfits[i] + rightMaxProfits[i])
    return rev

#    dp = [None] * 4
#    for i in range(0, 4):
#        dp[i] = [None] * len(prices)
#    return maxProfitDp(0, prices, 0, dp)

def maxProfitDp(priceIndex, prices, operation, dp):
    if operation == 4 or priceIndex == len(prices):
        return 0

    if dp[operation][priceIndex] == None:
        doNothingProfit = maxProfitDp(priceIndex + 1, prices, operation, dp)
        doOperationProfit = (-1 if operation % 2 == 0 else 1) * prices[priceIndex] + maxProfitDp(priceIndex + 1, prices, operation + 1, dp)
        dp[operation][priceIndex] = max(doNothingProfit, doOperationProfit)
    return dp[operation][priceIndex]

print(maxProfit([3,3,5,0,0,3,1,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))

