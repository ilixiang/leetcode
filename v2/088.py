#!/usr/bin/python3

def merge(nums1, m, nums2, n):
    i, j = m - 1, n - 1
    c = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[c] = nums1[i]
            i -= 1
        else:
            nums1[c] = nums2[j]
            j -= 1
        c -= 1
    
    while j >= 0:
        nums1[c] = nums2[j]
        j -= 1
        c -= 1
