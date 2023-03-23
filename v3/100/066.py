#!/usr/bin/python3

def plusOne(digits):
    c = 1
    i = len(digits) - 1
    while i >= 0 and c != 0:
        s = digits[i] + c
        digits[i] = s % 10
        c = s // 10
        i -= 1
    
    if c != 0:
        digits.insert(0, c)
    return digits
