#!/usr/bin/python3

import heapq

def kSmallestPairs(nums1, nums2, k):
    heap = [(nums1[0] + nums2[0], 0, 0)]
    print(len(nums1), len(nums2))
    rev = [None] * k
    visited = set([(0, 0)])
    i = 0
    while i < k and len(heap) > 0:
        (s, i1, i2) = heappop(heap)
        rev[i] = [nums1[i1], nums2[i2]]
        if i1 + 1 < len(nums1) and not (i1 + 1, i2) in visited:
            visited.add((i1 + 1, i2))
            heappush(heap, (nums1[i1 + 1] + nums2[i2], i1 + 1, i2))
        if i2 + 1 < len(nums2) and not (i1, i2 + 1) in visited:
            visited.add((i1, i2 + 1))
            heappush(heap, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
        i += 1
    return rev if i == k else rev[:i]
