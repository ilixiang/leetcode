#!/usr/bin/python3

import heapq

def nthUglyNumber(n):
    heap = [1]
    cnt = 1
    s = set(heap)
    while cnt != n:
        smallest = heapq.heappop(heap)
        cnt += 1
        for factor in [2, 3, 5]:
            candidate = factor * smallest
            if not candidate in s:
                heapq.heappush(heap, candidate)
                s.add(candidate)
    return heapq.heappop(heap)

