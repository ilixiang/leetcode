#!/usr/bin/python3

def trailingZeros(n):
    rev = 0
    while n != 0:
        n //= 5
        rev += n
    return rev
