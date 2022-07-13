#!/usr/bin/python3

def isUgly(n):
    if n <= 0:
        return False

    if n == 1:
        return True

    if n % 2 == 0:
        return isUgly(n // 2)

    if n % 3 == 0:
        return isUgly(n // 3)

    if n % 5 == 0:
        return isUgly(n // 5)

    return False

