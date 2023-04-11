#!/usr/bin/python3

def containsNearbyDuplicate(nums, k):
    if k == 0:
        return False
    s = set()
    for i in range(len(nums)):
        num = nums[i]
        if num in s:
            return True
        if i >= k:
            s.remove(nums[i - k])
        s.add(num)
    return False
    