#!/usr/bin/python3

def addDigits(num):
    if num == 0:
        return 0
    remainder = num % 9
    return 9 if remainder == 0 else remainder
