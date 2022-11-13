#!/usr/bin/python3

def singleNumber(nums):
    rev = 0
    for i in range(0, 31):
        tmp = 0
        for num in nums:
            tmp += (num >> i) & 1
        rev |= (tmp % 3) << i
    negative = 0
    for num in nums:
        if num < 0:
            negative += 1
    return rev if negative % 3 == 0 else (-1 * ((1 << 31) - rev))
