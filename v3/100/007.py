#!/usr/bin/python3

def reverse(x):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -1 * 2 ** 31

    INT_MAX_QUOTIENT = INT_MAX // 10
    INT_MIN_QUOTIENT = INT_MIN // 10 + 1

    INT_MAX_REMAINDER = INT_MAX % 10
    INT_MIN_REMAINDER = INT_MIN % 10 - 10

    rev = 0
    if x > 0:
        while x != 0:
            remainder = x % 10
            if rev < INT_MAX_QUOTIENT or (rev == INT_MAX_QUOTIENT and remainder <= INT_MAX_REMAINDER):
                rev = rev * 10 + remainder
            else:
                return 0
            x //= 10
    elif x < 0:
        while x != 0:
            remainder = x % 10
            remainder = (remainder - 10) if remainder != 0 else 0
            if rev > INT_MIN_QUOTIENT or (rev == INT_MIN_QUOTIENT and remainder >= INT_MIN_REMAINDER):
                rev = rev * 10 + remainder
            else:
                return 0
            x = x // 10
            x = x + (1 if remainder != 0 else 0)
    else:
        rev = 0

    return rev

if __name__ == '__main__':
    assert reverse(-123) == -321
