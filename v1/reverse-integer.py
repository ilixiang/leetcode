#!/usr/bin/python3

def reverse(x):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    QUOTIENT_MAX = INT_MAX // 10
    QUOTIENT_MIN = INT_MIN // 10 + 1
    rev = 0
    positive = x >= 0
    if positive:
        while x != 0:
            remainder = x % 10
            if rev > QUOTIENT_MAX or (rev == QUOTIENT_MAX and remainder > 7):
                return 0
            x = x // 10
            rev = rev * 10 + remainder
    else:
        while x != 0:
            remainder = x % 10
            x = x // 10
            if remainder != 0:
                remainder = remainder - 10
                x = x + 1
            if rev < (QUOTIENT_MIN) or (rev == (QUOTIENT_MIN) and remainder < -8):
                return 0
            rev = rev * 10 + remainder
    return rev

print(reverse(123))
print(reverse(-123))

