#!/usr/bin/python3

def maximumGap(nums):
    length = len(nums)

    maxNum = max(nums)
    minNum = min(nums)
    if maxNum == minNum or len(nums) <= 2:
        return maxNum - minNum
    
    diff = maxNum - minNum
    bucketSize = diff // (length - 1) + (1 if diff % (length - 1) != 0 else 0)
    buckets = [[] for i in range(0, length)]
    for num in nums:
        buckets[(num - minNum) // bucketSize].append(num)
    
    rev = 0
    previousMax = minNum
    for bucket in buckets:
        if len(bucket) == 0:
            continue
        bucketMax = max(bucket)
        bucketMin = min(bucket)
        rev = max(rev, bucketMin - previousMax)
        previousMax = bucketMax
    return rev

    