#!/usr/bin/python3

def longestConsecutive(nums):
    if len(nums) == 0:
        return 0

    rev = 0
    s = set(nums)
    for num in nums:
        if not num in s:
            continue

        curSequeceLength = 1
        s.remove(num)
        left = num - 1
        while left in s:
            s.remove(left)
            curSequeceLength += 1
            left -= 1
        
        right = num + 1
        while right in s:
            s.remove(right)
            curSequeceLength += 1
            right += 1
        rev = max(rev, curSequeceLength)
    return rev

