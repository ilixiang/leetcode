#!/usr/bin/python3

def maxProduct(nums):
    rev = None
    positive = None
    negative = None
    for i in range(0, len(nums)):
        curPositive, curNegative = positive, negative
        num = nums[i]
        if num == 0:
            positive = None
            negative = None
        elif num > 0:
            positive = num if curPositive == None else (num * curPositive)
            negative = None if curNegative == None else (num * curNegative)
        else:
            positive = None if curNegative == None else (num * curNegative)
            negative = num if curPositive == None else (num * curPositive)
        rev = max(filter(lambda x: x != None, [rev, num, positive, negative]))
    
    return rev

