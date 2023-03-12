#!/usr/bin/python3

def numDecodings(s):
    m = len(s)
    dp = [None] * (m + 1)
    dp[m] = 1

    def numDecodingsDp(i):
        if dp[i] != None:
            return dp[i]
        
        c = s[i]
        if c == '0':
            dp[i] = 0
        elif i < m - 1 and (c == '1' or (c == '2' and int(s[i + 1]) <= 6)):
            dp[i] = numDecodingsDp(i + 1) + numDecodingsDp(i + 2)
        else:
            dp[i] = numDecodingsDp(i + 1)
        return dp[i]
    return numDecodingsDp(0)
