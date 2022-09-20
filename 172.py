#!/usr/bin/python3

def trailingZeros(n):
    rev = 0
    while n != 0:
        n = n // 5
        rev = rev + n
    return rev

