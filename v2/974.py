#!/usr/bin/python3

def subarraysDivByK(nums, k):
    lookup = [0] * k
    lookup[0] = 1

    s = 0
    rev = 0
    for num in nums:
        s += num
        remainder = s % k
        rev += lookup[remainder]
        lookup[remainder] += 1
    return rev
