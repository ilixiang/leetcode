#!/usr/bin/python3

def singleNumber(nums):
    rev = 0
    negative = 0
    for i in range(0, 32):
        tmp = 0
        for num in nums:
            if num < 0:
                negative += 1
                num = -num
            tmp += (num & (1 << i)) >> i
        rev |= (tmp % 3) << i
    if negative % 3 != 0:
        return -1 * rev
    return rev
