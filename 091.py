#!/usr/bin/python3

def numDecodings(s):
    dp = [None] * (len(s) + 1)
    dp[len(s)] = 1
    return numDecodingsDp(s, 0, dp)

def numDecodingsDp(s, start, dp):
    if dp[start] != None:
        return dp[start]

    if start == len(s):
        return 1

    if start + 1 < len(s) and (s[start] == '1' or (s[start] == '2' and s[start + 1] <= '6')):
        dp[start] = numDecodingsDp(s, start + 1, dp) + numDecodingsDp(s, start + 2, dp)
    elif s[start] == '0':
        dp[start] == 0
    else:
        dp[start] = numDecodingsDp(s, start + 1, dp)
    return dp[start]

print(numDecodings('12'))
print(numDecodings('226'))

