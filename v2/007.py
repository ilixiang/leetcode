#!/usr/bin/python3

def reverse(x):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    INT_MAX_REMAINDER = INT_MAX % 10
    INT_MAX_QUOTIENT = INT_MAX // 10

    INT_MIN_REMAINDER = INT_MIN % 10 - 10
    INT_MIN_QUOTIENT = INT_MIN // 10 + 1

    res = 0
    negative = x < 0
    if not negative:
        while x != 0:
            remainder = x % 10
            if res > INT_MAX_QUOTIENT or (res == INT_MAX_QUOTIENT and INT_MAX_REMAINDER < remainder):
                return 0
            res = res * 10 + remainder
            x = x // 10
    else:
        while x != 0:
            remainder = x % 10
            remainder = (remainder - 10) if remainder != 0 else 0
            if res < INT_MIN_QUOTIENT or (res == INT_MIN_QUOTIENT and INT_MIN_REMAINDER > remainder):
                return 0
            res = res * 10 + remainder
            x = x // 10 + (1 if remainder != 0 else 0)

    return res
