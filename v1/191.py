#!/usr/bin/python3

def hammingWeight(n):
    count = 0
    while n != 0:
        if n & 1 == 1:
            count = count + 1
        n = n >> 1
    return count

