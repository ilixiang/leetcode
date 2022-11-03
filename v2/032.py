#!/usr/bin/python3

def longestValidParentheses(s):
    stack = []
    dp = [None] * len(s)
    res = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            stack.append(i)
            dp[i] = 0
        else:
            if len(stack) == 0:
                dp[i] = 0
            else:
                leftIndex = stack.pop() 
                dp[i] = i - leftIndex + 1 + (dp[leftIndex - 1] if leftIndex > 0 else 0)
                res = max(res, dp[i])
    return res

