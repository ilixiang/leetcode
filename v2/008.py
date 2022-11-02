#!/usr/bin/python3

def myAtoi(s):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    INT_MAX_REMAINDER = INT_MAX % 10
    INT_MAX_QUOTIENT = INT_MAX // 10

    INT_MIN_REMAINDER = INT_MIN % 10 - 10
    INT_MIN_QUOTIENT = INT_MIN // 10 + 1


    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    if i == len(s):
        return 0
    
    positive = True
    if s[i] == '-':
        positive = False
        i += 1
    elif s[i] == '+':
        i += 1
    elif not s[i].isdecimal():
        return 0

    res = 0
    if positive:
        while i < len(s) and s[i].isdecimal():
            val = int(s[i])
            if res > INT_MAX_QUOTIENT or (res == INT_MAX_QUOTIENT and val > INT_MAX_REMAINDER):
                return INT_MAX
            res = res * 10 + val
            i += 1
    else:
        while i < len(s) and s[i].isdecimal():
            val = -1 * int(s[i])
            if res < INT_MIN_QUOTIENT or (res == INT_MIN_QUOTIENT and val < INT_MIN_REMAINDER):
                return INT_MIN
            res = res * 10 + val
            i += 1

    return res

