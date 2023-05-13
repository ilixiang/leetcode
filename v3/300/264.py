#!/usr/bin/python3

import heapq

def nthUglyNumber(n):
    s = set()
    queue = [1]
    while n != 1:
        ugly = heapq.heappop(queue)

        doubleUgly = 2 * ugly
        tripleUgly = 3 * ugly
        quintuple = 5 * ugly
        if not doubleUgly in s:
            heapq.heappush(queue, doubleUgly)
            s.add(doubleUgly)
        if not tripleUgly in s:
            heapq.heappush(queue, tripleUgly)
            s.add(tripleUgly)
        if not quintuple in s:
            heapq.heappush(queue, quintuple)
            s.add(quintuple)

        n -= 1
    return heapq.heappop(queue)
