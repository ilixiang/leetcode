#!/usr/bin/python3

from math import sqrt

def countPrime(n):
    if n < 2:
        return 0
    
    isPrimes = [True] * n
    for i in range(2, int(sqrt(n)) + 1):
        if not isPrimes[i]:
            continue
        for j in range(i * i, n, i):
            isPrimes[j] = False
    
    rev = 0
    for i in range(2, n):
        if isPrimes[i]:
            rev += 1
    return rev
