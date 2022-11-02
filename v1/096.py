#!/usr/bin/python3

def numTrees(n):
    dp = [None] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    return numTreesDp(n, dp)

def numTreesDp(n, dp):
    if dp[n] != None:
        return dp[n]

    count = 0
    for rootIndex in range(0, n):
        count = count + (numTreesDp(rootIndex, dp) * numTreesDp(n - rootIndex - 1, dp))
    dp[n] = count
    return count

print(numTrees(3))

