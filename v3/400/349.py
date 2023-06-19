#!/usr/bin/python3

def intersection(nums1, nums2):
    counts = [0] * 1001
    for num in nums1:
        counts[num] += 1
    rev = []
    for num in nums2:
        if counts[num] != 0:
            rev.append(num)
            counts[num] -= 1
    return rev
