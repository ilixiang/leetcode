#!/usr/bin/python3

def divide(dividend, divisor):
    if dividend == 0:
        return 0

    maxInt = 2 ** 31 - 1
    minInt = -1 * 2 ** 31

    positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0

    while dividend >= divisor:
        multipleDivisor = divisor
        quotientPart = 1
        while multipleDivisor <= dividend:
            multipleDivisor = multipleDivisor << 1
            quotientPart = quotientPart << 1
        dividend = dividend - (multipleDivisor >> 1)
        if positive and maxInt - quotient < (quotientPart >> 1):
            return maxInt
        if not positive and minInt + quotient > -1 * (quotientPart >> 1):
            return minInt
        quotient = quotient + (quotientPart >> 1)

    return quotient if positive else -quotient

print(divide(100, 9))
print(divide(-100, 9))
print(divide(99, 9))
print(divide(-99, 9))
print(divide(-2147483648, -1))

