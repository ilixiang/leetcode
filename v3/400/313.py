#!/usr/bin/python3

import heapq

def nthSuperUglyNumber(n, primes):
    h = [1]
    while n > 1:
        val = heapq.heappop(h)
        for prime in primes:
            heapq.heappush(h, val * prime)
            if val % prime == 0:
                break
        n -= 1
    return heapq.heappop(h)
