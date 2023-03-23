#!/usr/bin/python3

def longestConsecutive(nums):
    s = set(nums)
    visited = set()
    rev = 0
    for num in nums:
        if num in visited:
            continue
        visited.add(num)

        left = num - 1
        while left in s:
            visited.add(left)
            left -= 1

        right = num + 1
        while right in s:
            visited.add(right)
            right += 1
        rev = max(rev, right - left - 1)
    return rev
