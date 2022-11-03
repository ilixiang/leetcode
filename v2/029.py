#!/usr/bin/python3

def divide(dividend, divisor):
    MAX_INT = 2 ** 31 - 1
    MIN_INT = -2 ** 31

    if dividend == 0:
        return 0
    if divisor == 1:
        return dividend
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    negative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
    quotient = 0
    dividend = dividend if dividend > 0 else (0 - dividend)
    divisor = divisor if divisor > 0 else (0 - divisor)
    while dividend >= divisor:
        shift = 0
        shiftedDividend = dividend
        while (shiftedDividend >> 1) >= divisor:
            shiftedDividend = shiftedDividend >> 1
            shift += 1
        quotient += 1 << shift
        dividend -= divisor << shift
    return quotient if not negative else (0 - quotient)



if __name__ == '__main__':
    print(divide(10, 3))
    print(divide(-10, 3))
    print(divide(10, -3))
    print(divide(-10, -3))
