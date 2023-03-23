#!/usr/bin/python3

def myAtoi(s):
    i = 0
    positive = True
    # ignore leading whitespaces
    while i < len(s) and s[i] == ' ':
        i += 1
    
    if i == len(s):
        return 0
    
    # check '-' and '+'
    if s[i] == '-':
        positive = False
        i += 1
    elif s[i] == '+':
        i += 1

    INT_MAX = 2 ** 31 - 1
    INT_MIN = -1 * 2 ** 31
    INT_MAX_QUOTIENT = INT_MAX // 10
    INT_MIN_QUOTIENT = INT_MIN // 10 + 1
    INT_MAX_REMAINDER = INT_MAX % 10
    INT_MIN_REMAINDER = INT_MIN % 10 - 10

    rev = 0
    # read until finding non-digit character or end of s
    while i < len(s) and s[i].isdigit():
        num = int(s[i])
        if positive:
            if rev < INT_MAX_QUOTIENT or (rev == INT_MAX_QUOTIENT and num <= INT_MAX_REMAINDER):
                rev = rev * 10 + num
            else:
                return INT_MAX
        else:
            if rev > INT_MIN_QUOTIENT or (rev == INT_MIN_QUOTIENT and -1 * num >= INT_MIN_REMAINDER):
                rev = rev * 10 - num
            else:
                return INT_MIN
        i += 1
    return rev
