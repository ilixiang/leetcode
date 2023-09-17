#!/usr/bin/python3

def largestDivisibleSubset(nums):
    nums.sort()
    mem = [(-1, 1)] * len(nums)
    maxCount = 1
    maxCountIdx = 0
    for i in range(len(nums)):
        num = nums[i]
        (prev, count) = mem[i]
        for j in range(i):
            if num % nums[j] == 0 and mem[j][1] + 1 > count:
                prev, count = j, mem[j][1] + 1
        mem[i] = (prev, count)
        if count > maxCount:
            maxCount = count
            maxCountIdx = i
    rev = [0] * maxCount
    while maxCountIdx != -1:
        rev[maxCount - 1] = nums[maxCountIdx]
        maxCountIdx = mem[maxCountIdx][0]
        maxCount -= 1
    return rev
