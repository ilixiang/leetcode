#!/usr/bin/python3

def numDistinct(s, t):
    m, n = len(s), len(t)
    dp = [[None for j in range(n)] for i in range(m)]

    sMap = {}
    for i in range(m):
        array = sMap.get(s[i], None)
        if array == None:
            sMap[s[i]] = [i]
        else:
            array.append(i)

    def numDistinctDp(i, j):
        if j == n:
            return 1
        if m - i < n - j:
            return 0

        if dp[i][j] != None:
            return dp[i][j]

        rev = 0
        array = sMap.get(t[j], [])
        for pos in array:
            if pos < i:
                continue
            rev += numDistinctDp(pos + 1, j + 1)
        dp[i][j] = rev
        return rev
    return numDistinctDp(0, 0)
