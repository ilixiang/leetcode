#!/usr/bin/python3

def containsDuplicate(nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False

