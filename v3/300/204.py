#!/usr/bin/python3

from math import sqrt

def countPrime(n):
    if n < 2:
        return 0

    primes = [1] * n
    primes[0] = 0
    primes[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i] != 1:
            continue
        for j in range(i * i, n, i):
            primes[j] = 0
    
    return sum(primes)
