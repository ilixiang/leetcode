#!/usr/bin/python3

def numTrees(n):
    dp = [None] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    return numTreesDp(n, dp)

def numTreesDp(n, dp):
    if dp[n] != None:
        return dp[n]

    rev = 0
    for leftNodes in range(0, n):
        rightNodes = n - leftNodes - 1
        leftPosibility = numTreesDp(leftNodes, dp)
        rightPosibility = numTreesDp(rightNodes, dp)
        rev += leftPosibility * rightPosibility
    dp[n] = rev
    return rev
