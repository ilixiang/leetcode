#!/usr/bin/python3

import heapq

def topKFrequent(nums, k):
    m = {}
    for num in nums:
        count = m.get(num, 0)
        m[num] = count + 1
    
    heap = []
    for num in m:
        heap.append((-m[num], num))

    rev = heapq.nsmallest(heap, k)
    return list(map(lambda x: x[1], rev))
