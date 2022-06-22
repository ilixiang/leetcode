#!/usr/bin/python3

def longestValidParentheses(s):
    dp = [0]
    stack = []
    longest = 0
    for i in range(0, len(s)):
        c = s[i]
        if c == '(':
            stack.append((c, i))
            dp.append(0)
        else:
            if len(stack) == 0:
                dp.append(0)
            else:
                left = stack.pop()
                tmp = i - left[1] + 1 + dp[left[1]]
                longest = max(tmp, longest)
                dp.append(tmp)
    return longest

print(longestValidParentheses('(()'))
print(longestValidParentheses(')()())'))
print(longestValidParentheses('()(())'))

