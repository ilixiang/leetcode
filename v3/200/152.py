#!/usr/bin/python3

def maxProduct(nums):
    if len(nums) == 1:
        return nums[0]
    maxPositive = 0
    minNegative = 0

    rev = 0
    for num in nums:
        if num == 0:
            maxPositive = minNegative = 0
        elif num > 0:
            if maxPositive > 0:
                maxPositive *= num
            else:
                maxPositive = num
            
            if minNegative < 0:
                minNegative *= num
            else:
                minNegative = 0
        else:
            originalMinNegative = minNegative
            if maxPositive > 0:
                minNegative = maxPositive * num
            else:
                minNegative = num
            
            if originalMinNegative < 0:
                maxPositive = originalMinNegative * num
            else:
                maxPositive = 0
        rev = max(rev, maxPositive)
    return rev
