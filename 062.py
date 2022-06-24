#!/usr/bin/python3

def uniquePath(m, n):
    dp = [None] * m
    for i in range(0, m):
        arr = [None] * n
        for j in range(0, n):
            if i == m - 1 or j == n - 1:
                arr[j] = 1
        dp[i] = arr
    print(dp)
    return uniquePathDp(0, 0, dp)
    
def uniquePathDp(mIndex, nIndex, dp):
    if dp[mIndex][nIndex] != None:
        return dp[mIndex][nIndex]

    dp[mIndex][nIndex] = uniquePathDp(mIndex + 1, nIndex, dp) + uniquePathDp(mIndex, nIndex + 1, dp)
    return dp[mIndex][nIndex]

print(uniquePath(3, 2))
print(uniquePath(3, 7))
print(uniquePath(1, 1))

