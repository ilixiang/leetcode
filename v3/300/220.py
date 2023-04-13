#!/usr/bin/python3

def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    m = {}
    n = valueDiff + 1
    for i in range(len(nums)):
        quotient = nums[i] // n
        if quotient in m:
            return True
        
        left = m.get(quotient - 1, None)
        if left != None and abs(nums[i] - left) <= valueDiff:
            return True

        right = m.get(quotient + 1, None)
        if right != None and abs(nums[i] - right) <= valueDiff:
            return True

        m[quotient] = nums[i]
        if i >= indexDiff:
            del m[nums[i - indexDiff] // n]
    return False
