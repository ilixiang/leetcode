#!/usr/bin/python3

def plusOne(digits):
    carry = 1
    i = len(digits) - 1
    while i >= 0 and carry != 0:
        s = digits[i] + 1
        digits[i] = s % 10
        carry = s // 10
        i -= 1
    if carry == 0:
        return digits
    res = [carry]
    res.extend(digits)
    return res
