#!/usr/bin/python3

from functools import reduce

def productExceptSelf(nums):
    zeroCount = sum(map(lambda n: 0 if n != 0 else 1, nums))
    if zeroCount > 1:
        return [0] * len(nums)
    elif zeroCount == 1:
        product = reduce(lambda a, b: a * b, filter(lambda n: n != 0, nums))
        return list(map(lambda n: product if n == 0 else 0, nums))
    else:
        product = reduce(lambda a, b: a * b, filter(lambda n: n != 0, nums))
        return list(map(lambda n: product // n, nums))
