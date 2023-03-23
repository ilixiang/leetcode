#!/usr/bin/python3

def longestValidParenthesis(s):
    maxMatches = [0 for i in range(len(s))]
    match = 0
    rev = 0
    stack = []
    for i in range(len(s)):
        c = s[i]
        if c == '(':
            stack.append(i)
            match = 0
        else:
            if len(stack) != 0:
                leftBraceIndex = stack.pop()
                match = match + maxMatches[leftBraceIndex - 1] + 2
                maxMatches[i] = match
                rev = max(rev, match)
            else:
                match = 0
                maxMatches[i] = match
    return rev
