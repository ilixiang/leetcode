#!/usr/bin/python3

def containsNearbyDuplicate(nums, k):
    lastIndexMap = {}
    for i in range(0, len(nums)):
        num = nums[i]
        if num in lastIndexMap and (i - lastIndexMap[num]) <= k:
            return True
        lastIndexMap[num] = i
    return False


