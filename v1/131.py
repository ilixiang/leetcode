#!/usr/bin/python3

def partition(s):
    length = len(s)
    dp = [None] * length
    for i in range(0, length):
        dp[i] = [None] * length

    rev = []
    partitionDp(s, 0, dp, rev, [])
    return rev

def partitionDp(s, start, dp, res, stack):
    if start == len(s):
        res.append(list(stack))
        return

    for i in range(start, len(s)):
        if isPalindromeDp(s, start, i, dp):
            stack.append(s[start:i + 1])
            partitionDp(s, i + 1, dp, res, stack)
            stack.pop()
            
def isPalindromeDp(s, start, end, dp):
    if start >= end:
        return True
    if dp[start][end] == None:
        dp[start][end] = isPalindromeDp(s, start + 1, end - 1, dp) if s[start] == s[end] else False
    return dp[start][end]

print(partition('aab'))
