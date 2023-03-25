#!/usr/bin/python3

from math import ceil

def maximumGap(nums):
    if len(nums) == 0:
        return 0

    buckets = [] * (len(nums) + 1)
    maxNum = max(nums)
    minNum = min(nums)
    interval = ceil((maxNum - minNum) // len(nums))

    for num in nums:
        index = (num - minNum) // interval
        slot = buckets[index]
        if not slot:
            slot = buckets[index] = [num, num]
        else:
            slot[0] = min(slot[0], num)
            slot[1] = max(slot[1], num)
    
    rev = 0
    prevMax = minNum
    for bucket in buckets:
        if not bucket:
            continue
        rev = max(rev, bucket[0] - prevMax)
        prevMax = bucket[1]
    return rev
        
