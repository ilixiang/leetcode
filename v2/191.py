#!/usr/bin/python3

def hammingWeight(n):
    rev = 0
    while n != 0:
        rev += n & 1
        n >>= 1
    return rev

