#!/usr/bin/python3

def majorityElement(nums):
    m = {}
    for num in nums:
        if not num in m:
            m[num] = 1
        m[num] = m[num] + 1
        if m[num] > (n // 2):
            return num

def boyerMooreVoting(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count = count + (1 if candidate == num else -1)
    return candidate

