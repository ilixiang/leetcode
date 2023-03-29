#!/usr/bin/python3

def rangeBitwiseAnd(left, right):
    diff = right - left
    rev = left
    offset = 0
    while rev != 0 and (1 << offset) - (left & ((1 << offset) - 1)) <= diff:
        rev &= ~(1 << offset)
        offset += 1
    return rev
